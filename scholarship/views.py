import os

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django_ratelimit.decorators import ratelimit
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from braces.views import LoginRequiredMixin
from openpyxl import Workbook
from .mixins import ModeratorsMixin

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
    UserFilterForm,
)
from scholarship.models import Attachments, TemporaryStorage


@method_decorator(
    ratelimit(key="user_or_ip", rate="5/m", method="GET", block=True), name="dispatch"
)
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
            return redirect("scholarship-application-attachments")

        return super().get(request, *args, **kwargs)

    def get_form(self, step=None, data=None, files=None):
        if step is None:
            step = self.steps.current

        # Retrieve any existing data for this step
        temp_data = {}
        try:
            temp_storage = TemporaryStorage.objects.get(
                step=step, user=self.request.user
            )
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
            step=self.steps.current, user=self.request.user, defaults={"data": data}
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

        from_email = os.getenv("DEFAULT_FROM_EMAIL", default="")

        default_from_email = f"Rosa Parks Scholarship Foundation {from_email}"

        # Send confirmation email
        send_mail(
            "Scholarship Application Confirmation",
            "Your scholarship application has been received.",
            default_from_email,
            [self.request.user.email],
            fail_silently=False,
        )

        # Redirect the user to a success page
        return HttpResponseRedirect("/scholarship/application/attachments/")


@method_decorator(
    ratelimit(key="user_or_ip", rate="5/m", method="GET", block=True), name="dispatch"
)
class AttachmentView(LoginRequiredMixin, CreateView):
    template_name = "scholarship/attachments.html"
    model = Attachments
    form_class = AttachmentForm
    success_url = "/scholarship/application/success/"

    def get(self, request, *args, **kwargs):
        if not self.request.user.has_submitted_application:
            return redirect("scholarship-application")
        elif not self.request.user.has_submitted_attachments:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("scholarship-application-success")

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.request.user.has_submitted_attachments = True
        self.request.user.save()
        return super().form_valid(form)


@method_decorator(
    ratelimit(key="user_or_ip", rate="5/m", method="GET", block=True), name="dispatch"
)
class UserScholarshipListView(LoginRequiredMixin, ModeratorsMixin, ListView):
    model = get_user_model()
    template_name = "scholarship/user_scholarship_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = UserFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = UserFilterForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data["has_submitted_application"] == "true":
                queryset = queryset.filter(has_submitted_application=True)
            elif form.cleaned_data["has_submitted_application"] == "false":
                queryset = queryset.filter(has_submitted_application=False)
            if form.cleaned_data["has_submitted_attachments"] == "true":
                queryset = queryset.filter(has_submitted_attachments=True)
            elif form.cleaned_data["has_submitted_attachments"] == "false":
                queryset = queryset.filter(has_submitted_attachments=False)
            if form.cleaned_data["completed_application"] == "true":
                queryset = queryset.filter(
                    has_submitted_application=True, has_submitted_attachments=True
                )
        return queryset


@method_decorator(
    ratelimit(key="user_or_ip", rate="5/m", method="GET", block=True), name="dispatch"
)
class DownloadExcelView(LoginRequiredMixin, ModeratorsMixin, View):
    def post(self, request, *args, **kwargs):
        user_ids = request.POST.getlist("user_ids")
        users = get_user_model().objects.filter(id__in=user_ids)

        wb = Workbook()
        ws = wb.active
        ws.append(
            [
                "First Name",
                "Last Name",
                "Email",
                "Address 1",
                "Address 2",
                "City",
                "State",
                "Zip Code",
                "Phone Number",
                "Date of Birth",
                "Place of Birth",
                "High School Name",
                "High School City",
                "High School Graduation Date",
                "High School GPA",
                "Academic Counselor Name",
                "Academic Counselor Phone Number",
                "Academic Counselor Email",
                "Current Employer Name",
                "Current Job Title",
                "Hours Per Week",
                "Parent 1 Full Name",
                "Parent 1 Email",
                "Parent 1 Address 1",
                "Parent 1 Address 2",
                "Parent 1 City",
                "Parent 1 State",
                "Parent 1 Zip Code",
                "Parent 1 Phone Number",
                "Parent 1 Place of Employment",
                "Parent 1 Job Title",
                "Parent 2 Full Name",
                "Parent 2 Email",
                "Parent 2 Address 1",
                "Parent 2 Address 2",
                "Parent 2 City",
                "Parent 2 State",
                "Parent 2 Zip Code",
                "Parent 2 Phone Number",
                "Parent 2 Place of Employment",
                "Parent 2 Job Title",
                "Total Household Income",
                "Number of Siblings Under 18",
                "Number of Siblings Over 18",
                "College Goal",
                "College Major",
                "College Career",
                "College Applied for #1",
                "College Applied for #2",
                "College Applied for #3",
                "College Plan to Attend",
                "College Savings",
                "College Savings by Guardian",
                "College Financial Need",
                "Foster Care",
                "Challenges",
                "Other Scholarships Applied For",
                "Other Scholarships Awarded",
                "Plan to Pay",
            ]
        )
        for user in users:
            ws.append(
                [
                    user.first_name,
                    user.last_name,
                    user.email,
                    getattr(user.personalinformation, "address1", "")
                    if hasattr(user, "personalinformation")
                    else "",
                    getattr(user.personalinformation, "address2", "")
                    if hasattr(user, "personalinformation")
                    else "",
                    getattr(user.personalinformation, "city", "")
                    if hasattr(user, "personalinformation")
                    else "",
                    getattr(user.personalinformation, "state", "")
                    if hasattr(user, "personalinformation")
                    else "",
                    getattr(user.personalinformation, "zip_code", "")
                    if hasattr(user, "personalinformation")
                    else "",
                    getattr(user.personalinformation, "phone_number.raw_input", "")
                    if hasattr(user, "personalinformation")
                    else "",
                    getattr(user.personalinformation, "dob", "")
                    if hasattr(user, "personalinformation")
                    else "",
                    getattr(user.personalinformation, "place_of_birth", "")
                    if hasattr(user, "personalinformation")
                    else "",
                    getattr(user.highschool, "name", "")
                    if hasattr(user, "highschool")
                    else "",
                    getattr(user.highschool, "city", "")
                    if hasattr(user, "highschool")
                    else "",
                    getattr(user.highschool, "graduation_date", "")
                    if hasattr(user, "highschool")
                    else "",
                    getattr(user.highschool, "gpa", "")
                    if hasattr(user, "highschool")
                    else "",
                    getattr(user.academiccounselor, "name", "")
                    if hasattr(user, "academiccounselor")
                    else "",
                    getattr(user.academiccounselor, "phone_number.raw_input", "")
                    if hasattr(user, "academiccounselor")
                    else "",
                    getattr(user.academiccounselor, "email", "")
                    if hasattr(user, "academiccounselor")
                    else "",
                    getattr(user.currentemployment, "name", "")
                    if hasattr(user, "currentemployment")
                    else "",
                    getattr(user.currentemployment, "job_title", "")
                    if hasattr(user, "currentemployment")
                    else "",
                    getattr(user.currentemployment, "hours_per_week", "")
                    if hasattr(user, "currentemployment")
                    else "",
                    getattr(user.parent, "parent_1_full_name", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_email", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_address1", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_address2", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_city", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_state", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_zip_code", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_phone_number.raw_input", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_place_of_employment", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_1_job_title", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_full_name", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_email", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_address1", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_address2", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_city", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_state", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_zip_code", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_phone_number.raw_input", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_place_of_employment", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.parent, "parent_2_job_title", "")
                    if hasattr(user, "parent")
                    else "",
                    getattr(user.household, "total_household_income", "")
                    if hasattr(user, "household")
                    else "",
                    getattr(user.household, "siblings_under_18", "")
                    if hasattr(user, "household")
                    else "",
                    getattr(user.household, "siblings_over_18", "")
                    if hasattr(user, "household")
                    else "",
                    getattr(user.college, "goal", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "major", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "career", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "applied_for_1", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "applied_for_2", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "applied_for_3", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "plan_to_attend", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "savings", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "savings_by_guardian", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.college, "financial_need", "")
                    if hasattr(user, "college")
                    else "",
                    getattr(user.other, "foster_care", "")
                    if hasattr(user, "other")
                    else "",
                    getattr(user.other, "challenges", "")
                    if hasattr(user, "other")
                    else "",
                    getattr(user.other, "other_scholarships", "")
                    if hasattr(user, "other")
                    else "",
                    getattr(user.other, "other_scholarships_awarded", "")
                    if hasattr(user, "other")
                    else "",
                    getattr(user.other, "plan_to_pay", "")
                    if hasattr(user, "other")
                    else "",
                ]
            )

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = "attachment; filename=users.xlsx"
        wb.save(response)

        return response
