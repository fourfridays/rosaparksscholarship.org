from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from phonenumber_field.formfields import PhoneNumberField

from .models import User
from constants import CONTIGUOUS_STATES_CHOICES


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=60, label="First Name")
    last_name = forms.CharField(max_length=60, label="Last Name")
    phone_number = PhoneNumberField(region="US")
    dob = forms.DateField(widget=forms.SelectDateWidget(), label="Date of Birth")
    address1 = forms.CharField(max_length=1024, label="Address line 1")
    address2 = forms.CharField(max_length=1024, label="Address line 2", required=False)
    city = forms.CharField(max_length=1024)
    state = forms.ChoiceField(choices=CONTIGUOUS_STATES_CHOICES)
    zip_code = forms.CharField(max_length=12)
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.dob = self.cleaned_data["dob"]
        user.address1 = self.cleaned_data["address1"]
        user.address2 = self.cleaned_data["address2"]
        user.city = self.cleaned_data["city"]
        user.state = self.cleaned_data["state"]
        user.zip_code = self.cleaned_data["zip_code"]
        user.save()
        return user
