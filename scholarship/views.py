from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin

from formtools.wizard.views import SessionWizardView
from scholarship.forms import (
    PersonalInformationForm,
    HighSchoolForm,
    StudentEmploymentHistoryForm,
    ParentForm,
    HouseholdForm,
)
from page.storage_backends import PrivateMediaStorage
from scholarship.models import TemporaryStorage
from users.models import User


class ScholarshipView(LoginRequiredMixin, SessionWizardView):
    form_list = [
        PersonalInformationForm,
        HighSchoolForm,
        StudentEmploymentHistoryForm,
        ParentForm,
        HouseholdForm,
    ]
    template_name = "scholarship/index.html"
    file_storage = PrivateMediaStorage()

    def get(self, request, *args, **kwargs):
        if self.request.user.has_submitted_application:
            return redirect('scholarship-success')
        
        return super().get(request, *args, **kwargs)

    def get_form(self, step=None, data=None, files=None):
        if step is None:
            step = self.steps.current

        # Retrieve any existing data for this step
        temp_data = {}
        try:
            temp_storage = TemporaryStorage.objects.get(step=step, user=self.request.user)
            temp_data = temp_storage.data
            print(temp_data, data)
            # Merge the POST data and the TemporaryStorage data
            if data is not None:
                data = data
            else:
                data = temp_data
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

        high_school_form = form_list[1]
        if high_school_form.cleaned_data:
            high_school = high_school_form.save(commit=False)
            high_school.user = self.request.user
            high_school.save()

        student_employment_history_form = form_list[2]
        if student_employment_history_form.cleaned_data:
            student_employment_history = student_employment_history_form.save(commit=False)
            student_employment_history.user = self.request.user
            student_employment_history.save()

        parent_form = form_list[3]
        if parent_form.cleaned_data:
            parent = parent_form.save(commit=False)
            parent.user = self.request.user
            parent.save()

        household_form = form_list[4]
        if household_form.cleaned_data:
            household = household_form.save(commit=False)
            household.user = self.request.user
            household.save()

        # Set the has_submitted_form flag in the user model to True
        self.request.user.has_submitted_application = True
        self.request.user.save()

        # Delete the TemporaryStorage records for the current user
        TemporaryStorage.objects.filter(user=self.request.user).delete()

        # Redirect the user to a success page
        return HttpResponseRedirect('/scholarship-application/success/')
