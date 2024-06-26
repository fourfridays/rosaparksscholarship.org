from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.dispatch import receiver

from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel

from users.models import User
from page.storage_backends import PrivateMediaStorage
from phonenumber_field.modelfields import PhoneNumberField
from constants import (
    HOUSEHOLD_INCOME_CHOICES,
    CONTIGUOUS_STATES_CHOICES,
    COUNTRY_CHOICES,
)


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
    place_of_birth = models.CharField(
        default="United States of America",
        choices=COUNTRY_CHOICES,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name_plural = "Personal Information"

    def __str__(self):
        return self.user.email


class HighSchool(models.Model):
    name = models.CharField("High School Name", max_length=120, default="None")
    city = models.CharField(
        "High School City",
        max_length=40,
        default="None",
        help_text="City where High School is Located",
    )
    graduation_date = models.DateField("High School Graduation Date")
    gpa = models.DecimalField(
        "High School GPA",
        max_digits=3,
        decimal_places=2,
        validators=[MaxValueValidator(5)],
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name_plural = "High School"

    def __str__(self):
        return f"{self.user.email}"


class AcademicCounselor(models.Model):
    name = models.CharField(
        "Academic Counselor Name",
        max_length=120,
        help_text="Enter name of counselor who can verify academic information",
    )
    phone_number = PhoneNumberField(
        "Academic Counselor Phone Number",
        region="US",
        help_text="Enter phone number of counselor who can verify academic information",
    )
    email = models.EmailField(
        "Academic Counselor Email Address",
        help_text="Enter email address of counselor who can verify academic information",
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name_plural = "Academic Counselor"

    def __str__(self):
        return f"{self.user.email}"


class CurrentEmployment(models.Model):
    employer_name = models.CharField(
        "Employer Name",
        max_length=120,
        null=True,
        blank=True,
    )
    job_title = models.CharField(
        "Job Title",
        max_length=40,
        null=True,
        blank=True,
    )
    hours_per_week = models.PositiveSmallIntegerField(
        "Hours Per Week",
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name_plural = "Current Employment"

    def __str__(self):
        return f"{self.user.email}"


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
    parent_1_place_of_employment = models.CharField(
        "Parent 1 Place of Employment",
        max_length=120,
        null=True,
        blank=True,
    )
    parent_1_job_title = models.CharField(
        "Parent 1 Job Title",
        max_length=40,
        null=True,
        blank=True,
    )

    parent_2_full_name = models.CharField(
        "Parent 2 Full Name (if applicable)", max_length=40, null=True, blank=True
    )
    parent_2_email = models.EmailField(
        "Parent 2 Email Address (if applicable)", null=True, blank=True
    )
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
    parent_2_phone_number = PhoneNumberField(
        "Parent 2 Phone Number (if applicable)", region="US", null=True, blank=True
    )
    parent_2_place_of_employment = models.CharField(
        "Parent 2 Place of Employment (if applicable)",
        max_length=120,
        null=True,
        blank=True,
    )
    parent_2_job_title = models.CharField(
        "Parent 2 Job Title (if applicable)", max_length=120, null=True, blank=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.user.email}"


class Household(models.Model):
    total_household_income = models.CharField(
        max_length=20, choices=HOUSEHOLD_INCOME_CHOICES
    )
    siblings_under_18 = models.PositiveSmallIntegerField(
        default=0, blank=True, null=True
    )
    siblings_over_18 = models.PositiveSmallIntegerField(
        default=0, blank=True, null=True
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name_plural = "Household"

    def __str__(self):
        return f"{self.user.email}"


class College(models.Model):
    goal = models.TextField(help_text="Educational Goal")
    major = models.CharField(max_length=120, help_text="College Major")
    career = models.CharField(
        max_length=120, help_text="Career/Profession (teacher, musician, lawyer, etc.)"
    )
    applied_for_1 = models.CharField(
        max_length=60, help_text="College/University you have applied to"
    )
    applied_for_2 = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text="College/University you have applied to",
    )
    applied_for_3 = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text="College/University you have applied to",
    )
    plan_to_attend = models.CharField(
        max_length=60, help_text="College/University you plan to attend"
    )
    savings = models.IntegerField(
        default=0, help_text="How much have you saved for college"
    )
    savings_by_guardian = models.IntegerField(
        default=0,
        help_text="How much have others (parents, grandparents, etc.) saved for your education",
    )
    financial_need = models.TextField(
        help_text="Describe your financial need for scholarship funds (very important - be very specific)"
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name_plural = "College"

    def __str__(self):
        return f"{self.user.email}"


class Other(models.Model):
    foster_care = models.BooleanField(
        default=False,
        help_text="Are you in the foster care system, or are you an emancipated minor? If so, please indicate yes (This answer does not impact the judging process).",
    )
    challenges = models.TextField(
        null=True,
        blank=True,
        help_text="If you answered yes to the last question, please briefly describe the challenges you have faced in your educational journey because of your experiences in foster care or as an emancipated minor.",
    )
    other_scholarships = models.TextField(
        help_text="Other scholarships you have applied for"
    )
    other_scholarships_awarded = models.TextField(
        help_text="Scholarships/grants you have already been awarded (name, amount and period of time covered)",
    )
    plan_to_pay = models.TextField(
        help_text="If granted this award, how do you plan to pay for the rest of your educational costs?"
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name_plural = "Other"

    def __str__(self):
        return f"{self.user.email}"


@register_snippet
class ApplicationState(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    panels = [
        FieldPanel('start_date'),
        FieldPanel('end_date'),
    ]

    class Meta:
        verbose_name_plural = "Application State"
    
    def __str__(self):
        return f"Application Open from {self.start_date} to {self.end_date}"
 
    def save(self, *args, **kwargs):
        if not self.pk and ApplicationState.objects.exists():
            # if you'll not check for self.pk 
            # then error will also raised in update of exists model
            raise ValidationError('There can be only one Application State instance')
        return super(ApplicationState, self).save(*args, **kwargs)


class TemporaryStorage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.CharField(max_length=50)
    data = models.JSONField()
    submission_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Temporary Storage"

    def __str__(self):
        return f"{self.user.email}, Step {int(self.step)+1}"


# This will return the user email for folder name in S3
def get_user_file_path(instance, filename, field_name):
    return f"{instance.user.email}/{field_name}-{filename}"


def get_user_file_path_for_reference_letter_1(instance, filename):
    return get_user_file_path(instance, filename, "reference-letter-1")


def get_user_file_path_for_reference_letter_2(instance, filename):
    return get_user_file_path(instance, filename, "reference-letter-2")


def get_user_file_path_for_high_school_transcript(instance, filename):
    return get_user_file_path(instance, filename, "high-school-transcript")


def get_user_file_path_honors_awards(instance, filename):
    return get_user_file_path(instance, filename, "honors-awards")


def get_user_file_path_extracurricular_activities(instance, filename):
    return get_user_file_path(instance, filename, "extracurricular-activities")


def get_user_file_path_community_service_activities(instance, filename):
    return get_user_file_path(instance, filename, "community-service-activities")


def get_user_file_path_for_essay(instance, filename):
    return get_user_file_path(instance, filename, "essay")


class Attachments(models.Model):
    reference_letter_1 = models.FileField(
        upload_to=get_user_file_path_for_reference_letter_1,
        storage=PrivateMediaStorage(),
    )
    reference_letter_2 = models.FileField(
        upload_to=get_user_file_path_for_reference_letter_2,
        storage=PrivateMediaStorage(),
    )
    high_school_transcript = models.FileField(
        upload_to=get_user_file_path_for_high_school_transcript,
        storage=PrivateMediaStorage(),
    )
    honors_awards = models.FileField(
        upload_to=get_user_file_path_honors_awards,
        storage=PrivateMediaStorage(),
    )
    extracurricular_activities = models.FileField(
        upload_to=get_user_file_path_extracurricular_activities,
        storage=PrivateMediaStorage(),
    )
    community_service_volunteer_activities = models.FileField(
        upload_to=get_user_file_path_community_service_activities,
        storage=PrivateMediaStorage(),
    )
    essay = models.FileField(
        upload_to=get_user_file_path_for_essay,
        storage=PrivateMediaStorage(),
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name_plural = "Attachments"

    def __str__(self):
        return f"{self.user.email}"


# Delete reference attachments from AWS S3 upon deletion of scholarship application
@receiver(models.signals.post_delete, sender=Attachments)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.reference_letter_1.delete(save=False)
    instance.reference_letter_2.delete(save=False)
    instance.high_school_transcript.delete(save=False)
    instance.honors_awards.delete(save=False)
    instance.extracurricular_activities.delete(save=False)
    instance.community_service_volunteer_activities.delete(save=False)
    instance.essay.delete(save=False)
