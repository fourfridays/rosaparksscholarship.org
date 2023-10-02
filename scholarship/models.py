from django.db import models
from django.dispatch import receiver

from users.models import User
from page.storage_backends import PrivateMediaStorage


# This will return the user id for setting folder name in S3
def get_user_file_path(instance, filename):
    return f"{instance.user.email}/{filename}"


class EmploymentHistory(models.Model):
    employer_name = models.CharField(max_length=160)
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


# Delete attachments from AWS S3 upon deletion of scholarship application
@receiver(models.signals.post_delete, sender=EmploymentHistory)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.reference_letter_1.delete(save=False)
    instance.reference_letter_2.delete(save=False)
