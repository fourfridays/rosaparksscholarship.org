from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from users.models import User
from formtools.wizard.views import SessionWizardView
from scholarship.forms import (
    PersonalInformationForm,
    EmploymentHistoryForm,
    FamilyInformationForm,
)
from page.storage_backends import PrivateMediaStorage


class ScholarshipView(LoginRequiredMixin, SessionWizardView):
    form_list = [PersonalInformationForm, EmploymentHistoryForm, FamilyInformationForm]
    template_name = "scholarship/index.html"
    file_storage = PrivateMediaStorage()

    def done(self, form_list, **kwargs):
        personal_information_form = form_list[0]
        if personal_information_form.cleaned_data:
            personal_information = personal_information_form.save(commit=False)
            personal_information.user = User.objects.get(email=self.request.user)
            personal_information.save()

        employment_history_form = form_list[1]
        if employment_history_form.cleaned_data:
            employment_history = employment_history_form.save(commit=False)
            employment_history.user = User.objects.get(email=self.request.user)
            employment_history.save()

        family_information_form = form_list[2]
        if family_information_form.cleaned_data:
            family_information = family_information_form.save(commit=False)
            family_information.user = User.objects.get(email=self.request.user)
            family_information.save()

        for form in form_list:
            self.storage.set_step_data(form.step, self.process_step(form))

        return HttpResponse("Form Submitted")
