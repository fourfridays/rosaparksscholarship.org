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
)
from constants import (
    COUNTRY_CHOICES,
)


def date_minus_18_years():
    """Return 18 years from today"""
    now = datetime.datetime.now()
    return now - relativedelta(years=18)


class PersonalInformationForm(forms.ModelForm):
    title = "Personal Information Form"
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "MI",
                "disabled": True,
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
        label="Date of Birth"
    )
    place_of_birth = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        initial="US",
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
        label="Place of Birth"
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

