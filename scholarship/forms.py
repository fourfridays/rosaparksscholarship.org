import datetime

from django import forms
from django.utils.translation import gettext_lazy as _

from dateutil.relativedelta import relativedelta

from scholarship.models import PersonalInformation, EmploymentHistory, FamilyInformation


def date_minus_18_years():
    """Return 18 years from today"""
    now = datetime.datetime.now()
    return now - relativedelta(years=18)


class PersonalInformationForm(forms.ModelForm):
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
    class Meta:
        model = EmploymentHistory
        exclude = ["user"]


class FamilyInformationForm(forms.ModelForm):
    class Meta:
        model = FamilyInformation
        exclude = ["user"]
