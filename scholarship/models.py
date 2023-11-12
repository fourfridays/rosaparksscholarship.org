from django.db import models
from django.dispatch import receiver

from users.models import User
from page.storage_backends import PrivateMediaStorage
from phonenumber_field.modelfields import PhoneNumberField
from constants import HOUSEHOLD_INCOME_CHOICES, CONTIGUOUS_STATES_CHOICES


# This will return the user email for folder name in S3
def get_user_file_path(instance, filename):
    return f"{instance.user.email}/{filename}"


class PersonalInformation(models.Model):
    address1 = models.CharField(
        "Address line 1",
        max_length=35,
    )
    address2 = models.CharField(
        "Address line 2",
        max_length=35,
        null=True,
        blank=True,
    )
    city = models.CharField(
        "City",
        max_length=30,
    )
    state = models.CharField(
        max_length=20,
        default="MI",
    )
    zip_code = models.CharField(
        "ZIP",
        max_length=12,
    )
    phone_number = PhoneNumberField(region="US")
    dob = models.DateField()
    high_school = models.CharField(max_length=120, default="None")
    high_school_city = models.CharField(max_length=40, default="None")
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    class Meta:
        verbose_name_plural = "Personal Information"

    def __str__(self):
        return self.user.email


class StudentEmploymentHistory(models.Model):
    employer_name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=40)
    hours_per_week = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    class Meta:
        verbose_name_plural = "Employment History"

    def __str__(self):
        return f"{self.user.email}"

        """    reference_letter_1 = models.FileField(
        upload_to=get_user_file_path,
        storage=PrivateMediaStorage(),
    )
    reference_letter_2 = models.FileField(
        upload_to=get_user_file_path,
        storage=PrivateMediaStorage(),
        blank=True,
        null=True,
    )

        Returns:
            _type_: _description_
        """
# Delete reference attachments from AWS S3 upon deletion of scholarship application
# @receiver(models.signals.post_delete, sender=EmploymentHistory)
# def remove_file_from_s3(sender, instance, using, **kwargs):
#     instance.reference_letter_1.delete(save=False)
#     instance.reference_letter_2.delete(save=False)


class Parent(models.Model):
    parent_1_full_name = models.CharField("Parent 1 Full Name", max_length=40)
    parent_1_email = models.EmailField("Parent 1 Email Address", blank=False)
    parent_1_address1 = models.CharField(
        "Parent 1 Address line 1",
        max_length=35,
    )
    parent_1_address2 = models.CharField(
        "Parent 1 Address line 2",
        max_length=35,
        null=True,
        blank=True,
    )
    parent_1_city = models.CharField(
        "Parent 1 City",
        max_length=30,
    )
    parent_1_state = models.CharField(
        "Parent 1 State",
        max_length=20,
        choices=CONTIGUOUS_STATES_CHOICES,
        default="MI",
    )
    parent_1_zip_code = models.CharField(
        "Parent 1 Zip Code",
        max_length=12,
    )
    parent_1_phone_number = PhoneNumberField("Parent 1 Phone Number", region="US")
    parent_1_place_of_employment = models.CharField("Parent 1 Place of Employment", max_length=120)
    parent_1_job_title = models.CharField("Parent 1 Job Title", max_length=40)
    
    parent_2_full_name = models.CharField("Parent 2 Full Name (if applicable)", max_length=40,  null=True, blank=True)
    parent_2_email = models.EmailField("Parent 2 Email Address (if applicable)", null=True, blank=True)
    parent_2_address1 = models.CharField(
        "Parent 2 Address line 1 (if applicable)", max_length=35, null=True, blank=True
    )
    parent_2_address2 = models.CharField(
        "Parent 2 Address line 2 (if applicable)",
        max_length=35,
        null=True,
        blank=True,
    )
    parent_2_city = models.CharField(
        "Parent 2 City (if applicable)",
        max_length=30,
        null=True,
        blank=True,
    )
    parent_2_state = models.CharField(
        "Parent 2 State (if applicable)",
        max_length=20,
        choices=CONTIGUOUS_STATES_CHOICES,
        default="MI",
        null=True,
        blank=True,
    )
    parent_2_zip_code = models.CharField(
        "Parent 2 Zip Code (if applicable)",
        max_length=12,
        null=True,
        blank=True,
    )
    parent_2_phone_number = PhoneNumberField("Parent 2 Phone Number (if applicable)", region="US", null=True, blank=True)
    parent_2_place_of_employment = models.CharField(
        "Parent 2 Place of Employment (if applicable)", max_length=120, null=True, blank=True
    )
    parent_2_job_title = models.CharField("Parent 2 Job Title (if applicable)", max_length=120, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    def __str__(self):
        return f"{self.user.email}"


class Household(models.Model):
    total_household_income = models.CharField(
        max_length=20,
        choices=HOUSEHOLD_INCOME_CHOICES
    )
    siblings_under_18 = models.PositiveSmallIntegerField()
    siblings_over_18 = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

    class Meta:
        verbose_name_plural = "Household"

    def __str__(self):
        return f"{self.user.email}"


class TemporaryStorage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.CharField(max_length=50)
    data = models.JSONField()

    class Meta:
        verbose_name_plural = "Temporary Storage"

    def __str__(self):
        return f"{self.user.email}, Step {int(self.step)+1}"
