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
        choices=CONTIGUOUS_STATES_CHOICES,
        default="MI",
    )
    zip_code = models.CharField(
        "ZIP",
        max_length=12,
    )
    phone_number = PhoneNumberField(region="US")
    dob = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Personal Information"

    def __str__(self):
        return self.user.email


class EmploymentHistory(models.Model):
    employer_name = models.CharField(max_length=120)
    job_title = models.CharField(max_length=40)
    hours_per_week = models.PositiveSmallIntegerField()
    reference_letter_1 = models.FileField(
        upload_to=get_user_file_path,
        storage=PrivateMediaStorage(),
    )
    reference_letter_2 = models.FileField(
        upload_to=get_user_file_path,
        storage=PrivateMediaStorage(),
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Employment History"

    def __str__(self):
        return self.user.email


# Delete reference attachments from AWS S3 upon deletion of scholarship application
@receiver(models.signals.post_delete, sender=EmploymentHistory)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.reference_letter_1.delete(save=False)
    instance.reference_letter_2.delete(save=False)


class FamilyInformation(models.Model):
    parent_1_full_name = models.CharField(max_length=40)
    parent_1_email = models.EmailField("email address", blank=False)
    parent_1_address1 = models.CharField(
        "Address line 1",
        max_length=35,
    )
    parent_1_address2 = models.CharField(
        "Address line 2",
        max_length=35,
        null=True,
        blank=True,
    )
    parent_1_city = models.CharField(
        "City",
        max_length=30,
    )
    parent_1_state = models.CharField(
        max_length=20,
        choices=CONTIGUOUS_STATES_CHOICES,
        default="MI",
    )
    parent_1_zip_code = models.CharField(
        "ZIP",
        max_length=12,
    )
    parent_1_phone_number = PhoneNumberField(region="US")
    parent_1_place_of_employment = models.CharField(max_length=120)
    parent_1_job_title = models.CharField(max_length=40)
    parent_2_full_name = models.CharField(max_length=40)
    parent_2_email = models.EmailField("email address", null=True, blank=True)
    parent_2_address1 = models.CharField(
        "Address line 1", max_length=35, null=True, blank=True
    )
    parent_2_address2 = models.CharField(
        "Address line 2",
        max_length=35,
        null=True,
        blank=True,
    )
    parent_2_city = models.CharField(
        "City",
        max_length=30,
        null=True,
        blank=True,
    )
    parent_2_state = models.CharField(
        max_length=20,
        choices=CONTIGUOUS_STATES_CHOICES,
        default="MI",
        null=True,
        blank=True,
    )
    parent_2_zip_code = models.CharField(
        "ZIP",
        max_length=12,
        null=True,
        blank=True,
    )
    parent_2_phone_number = PhoneNumberField(region="US", null=True, blank=True)
    parent_2_place_of_employment = models.CharField(
        max_length=120, null=True, blank=True
    )
    parent_2_job_title = models.CharField(max_length=120, null=True, blank=True)
    total_household_income = models.CharField(
        max_length=20,
        choices=HOUSEHOLD_INCOME_CHOICES
    )
    siblings = models.CharField(max_length=140)
    high_school = models.CharField(max_length=120)
    high_school_city = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Family Information"

    def __str__(self):
        return self.user.email
