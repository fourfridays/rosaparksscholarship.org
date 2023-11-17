import datetime

from django import forms
from django.utils.translation import gettext_lazy as _

from dateutil.relativedelta import relativedelta

from scholarship.models import (
    PersonalInformation,
    HighSchool,
    AcademicCounselor,
    CurrentEmployment,
    Parent,
    Household,
    College,
    Other,
    Attachments,
)
from scholarship.validators import file_size, validate_document_file_extension
from constants import (
    COUNTRY_CHOICES,
)


def date_minus_18_years():
    """Return 18 years from today"""
    now = datetime.datetime.now()
    return now - relativedelta(years=18)


class PersonalInformationForm(forms.ModelForm):
    title = "Personal Information"
    state = forms.CharField(
        initial="MI",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "MI",
                "readonly": True,
            },
        ),
        label="State (Applications are restricted to Michigan residents only)",
    )
    dob = forms.DateField(
        initial=date_minus_18_years(),
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
            },
        ),
        label="Date of Birth",
    )
    place_of_birth = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        initial="US",
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
        label="Place of Birth",
    )

    class Meta:
        model = PersonalInformation
        exclude = ["user"]


class HighSchoolForm(forms.ModelForm):
    title = "High School Information"
    graduation_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
            },
        ),
        label="High School Graduation Date",
    )
    gpa = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "0.00",
            },
        ),
        label="High School GPA",
    )

    class Meta:
        model = HighSchool
        exclude = ["user"]


class AcademicCounselorForm(forms.ModelForm):
    title = "Academic Counselor Form"

    class Meta:
        model = AcademicCounselor
        exclude = ["user"]


class CurrentEmploymentForm(forms.ModelForm):
    title = "Current Employment Information"

    class Meta:
        model = CurrentEmployment
        exclude = ["user"]


class ParentForm(forms.ModelForm):
    title = "Parent Form"

    class Meta:
        model = Parent
        exclude = ["user"]


class HouseholdForm(forms.ModelForm):
    title = "Household Form"
    siblings_under_18 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "0",
            },
        ),
        label="Number of siblings under 18",
        required=False,
    )
    siblings_over_18 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "0",
            },
        ),
        label="Number of siblings over 18",
        required=False,
    )

    class Meta:
        model = Household
        exclude = ["user"]


class CollegeForm(forms.ModelForm):
    title = "College Information"

    class Meta:
        model = College
        exclude = ["user"]


class OtherForm(forms.ModelForm):
    title = "Other Information"

    class Meta:
        model = Other
        exclude = ["user"]


class AttachmentForm(forms.ModelForm):
    title = "Attachments"
    reference_letter_1 = forms.FileField(
        label="Employer Reference Letter 1",
        validators=[file_size, validate_document_file_extension],
        help_text="Only PDF or DOC formats. Maximum file size is 2MiB.",
    )
    reference_letter_2 = forms.FileField(
        label="Employer Reference Letter 2",
        validators=[file_size, validate_document_file_extension],
        help_text="Only PDF or DOC formats. Maximum file size is 2MiB.",
        required=False,
    )
    high_school_transcript = forms.FileField(
        label="High School Transcript",
        validators=[file_size, validate_document_file_extension],
        help_text="Only PDF or DOC formats. Maximum file size is 2MiB.",
    )
    honors_awards = forms.FileField(
        label="Honors and Awards",
        validators=[file_size, validate_document_file_extension],
        help_text="Tell us about the honors and awards you received. Indicate whether they were on a local (school, county, or district), state or national level. These awards may be outside of school activities but should not be duplicated in any other section. Honor/Award, Year Received, Brief Description. Only PDF or DOC formats. Maximum file size is 2MiB.",
    )
    extracurricular_activities = forms.FileField(
        label="Extracurricular Activities",
        validators=[file_size, validate_document_file_extension],
        help_text="Extracurricular Activities (school, clubs, athletics). Indicate position(s), club(s) and/or athletics you participated in. Be sure to distinguish the grade year (9-12) and approximate hours you participated. Activity, Year Participated, Hours per Week, Brief Description. Only PDF or DOC formats. Maximum file size is 2MiB.",
    )
    community_service_volunteer_activities = forms.FileField(
        label="Community Service/Volunteer Activities",
        validators=[file_size, validate_document_file_extension],
        help_text="Community Service/Volunteer Activities (church, home, etc.).  List community organizations you actively participated in during each grade year (9-12).  Also, indicate hours of volunteer service for each activity.  These can be school-related but are not to be duplicated any in responses you made in any previous section of the application. Organization, Year Participated, Hours per Week, Brief Description. Only PDF or DOC formats. Maximum file size is 2MiB.",
    )
    essay = forms.FileField(
        validators=[file_size, validate_document_file_extension],
        help_text="Segregation was the defining social issue when Rosa Parks took her historic stand. Describe a social issue that you think should be addressed today. How will YOU use the principles of Rosa Parks to address it? Only PDF or DOC formats. Maximum file size is 2MiB.",
    )

    class Meta:
        model = Attachments
        exclude = ["user"]
