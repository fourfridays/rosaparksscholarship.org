from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from braces.views import LoginRequiredMixin

from formtools.wizard.views import SessionWizardView
from scholarship.forms import (
    PersonalInformationForm,
    HighSchoolForm,
    AcademicCounselorForm,
    CurrentEmploymentForm,
    ParentForm,
    HouseholdForm,
    CollegeForm,
    OtherForm,
    AttachmentForm,
)
from page.storage_backends import PrivateMediaStorage
from scholarship.models import Attachments, TemporaryStorage


class ScholarshipView(LoginRequiredMixin, SessionWizardView):
    form_list = [
        PersonalInformationForm,
        HighSchoolForm,
        AcademicCounselorForm,
        CurrentEmploymentForm,
        ParentForm,
        HouseholdForm,
        CollegeForm,
        OtherForm,
        AttachmentForm,
    ]
    template_name = "scholarship/index.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.has_submitted_application:
            return redirect('attachments')
        
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
        
        academic_counselor_form = form_list[2]
        if academic_counselor_form.cleaned_data:
            academic_counselor = academic_counselor_form.save(commit=False)
            academic_counselor.user = self.request.user
            academic_counselor.save()

        current_employment_form = form_list[3]
        if current_employment_form.cleaned_data:
            current_employment = current_employment_form.save(commit=False)
            current_employment.user = self.request.user
            current_employment.save()

        parent_form = form_list[4]
        if parent_form.cleaned_data:
            parent = parent_form.save(commit=False)
            parent.user = self.request.user
            parent.save()

        household_form = form_list[5]
        if household_form.cleaned_data:
            household = household_form.save(commit=False)
            household.user = self.request.user
            household.save()
        
        college_form = form_list[6]
        if college_form.cleaned_data:
            college = college_form.save(commit=False)
            college.user = self.request.user
            college.save()
        
        other_form = form_list[7]
        if other_form.cleaned_data:
            other = other_form.save(commit=False)
            other.user = self.request.user
            other.save()

        # Set the has_submitted_form flag in the user model to True
        self.request.user.has_submitted_application = True
        self.request.user.save()

        # Delete the TemporaryStorage records for the current user
        TemporaryStorage.objects.filter(user=self.request.user).delete()

        # Redirect the user to a success page
        return HttpResponseRedirect('/scholarship-application/success/')


class AttachmentView(LoginRequiredMixin, CreateView):
    template_name = "scholarship/attachments.html"
    model = Attachments
    form_class = AttachmentForm
    success_url = '/attachments/success/'
    
    def get(self, request, *args, **kwargs):
        if (not self.request.user.has_submitted_application):
            return redirect('scholarship-application')
        elif (not self.request.user.has_submitted_attachments):
            return super().get(request, *args, **kwargs)
        else:
            return redirect('scholarship-success')
        

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.request.user.has_submitted_attachments = True
        return super().form_valid(form)