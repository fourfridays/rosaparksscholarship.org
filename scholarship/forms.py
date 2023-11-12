import datetime

from django import forms
from django.utils.translation import gettext_lazy as _

from dateutil.relativedelta import relativedelta

from scholarship.models import (
    PersonalInformation,
    EmploymentHistory,
    Parent1,
    Parent2,
    Household,
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

    class Meta:
        model = PersonalInformation
        exclude = ["user"]


class EmploymentHistoryForm(forms.ModelForm):
    title = "Employment History Form"
    
    class Meta:
        model = EmploymentHistory
        exclude = ["user"]


class Parent1Form(forms.ModelForm):
    title = "Parent 1 Form"
    
    class Meta:
        model = Parent1
        exclude = ["user"]


class Parent2Form(forms.ModelForm):
    title = "Parent 2 Form"
    
    class Meta:
        model = Parent2
        exclude = ["user"]


class HouseholdForm(forms.ModelForm):
    title = "Household Form"
    
    class Meta:
        model = Household
        exclude = ["user"]
