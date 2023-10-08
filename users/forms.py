from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

from users.models import User


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
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user
