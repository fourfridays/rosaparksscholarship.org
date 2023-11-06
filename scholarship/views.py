from django.shortcuts import render
from django.views import View

from braces.views import LoginRequiredMixin

from formtools.wizard.views import SessionWizardView
from scholarship.forms import (
    PersonalInformationForm,
    EmploymentHistoryForm,
    Parent1Form,
    Parent2Form,
    HouseholdForm,
)
from page.storage_backends import PrivateMediaStorage
from scholarship.models import TemporaryStorage


class ScholarshipView(LoginRequiredMixin, SessionWizardView):
    form_list = [
        PersonalInformationForm,
        EmploymentHistoryForm,
        Parent1Form,
        Parent2Form,
        HouseholdForm,
    ]
    template_name = "scholarship/index.html"
    file_storage = PrivateMediaStorage()
    session_key = "my_wizard_view_data"

    def get_form(self, step=None, data=None, files=None):
        if step is None:
            step = self.steps.current

        # Retrieve any existing data for this step
        try:
            temp_storage = TemporaryStorage.objects.get(step=step, user=self.request.user)
            data = temp_storage.data
        except TemporaryStorage.DoesNotExist:
            pass

        return super().get_form(step, data, files)

    def process_step(self, form):        
        if form.is_valid():
            data = form.data
        
        if data is None:
            data = {}

        TemporaryStorage.objects.update_or_create(
            step=self.steps.current,
            user=self.request.user,
            defaults={'data': data}
        )

        return super().process_step(form)

    def done(self, form_list, **kwargs):
        personal_information_form = form_list[0]
        if personal_information_form.cleaned_data:
            personal_information = personal_information_form.save(commit=False)
            personal_information.user = self.request.user
            personal_information.save()

        employment_history_form = form_list[1]
        if employment_history_form.cleaned_data:
            employment_history = employment_history_form.save(commit=False)
            employment_history.user = self.request.user
            employment_history.save()

        parent_1_form = form_list[2]
        if parent_1_form.cleaned_data:
            parent_1 = parent_1_form.save(commit=False)
            parent_1.user = self.request.user
            parent_1.save()

        parent_2_form = form_list[3]
        if parent_2_form.cleaned_data:
            parent_2 = parent_2_form.save(commit=False)
            parent_2.user = self.request.user
            parent_2.save()

        household_form = form_list[4]
        if household_form.cleaned_data:
            household = household_form.save(commit=False)
            household.user = self.request.user
            household.save()

        #for form in form_list:
        #    self.storage.set_step_data(form.step, self.process_step(form))

        self.request.session[self.session_key] = self.get_all_cleaned_data()
        self.request.session.save()

        return super().done(form_list, **kwargs)
