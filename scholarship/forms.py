from django import forms

from scholarship.models import EmploymentHistory
from scholarship.validators import file_size, validate_document_file_extension


class EmploymentHistoryForm(forms.ModelForm):
    employer_name = forms.CharField(max_length=160)
    job_title = forms.CharField(max_length=40)
    hours_per_week = forms.IntegerField()
    reference_letter_1 = forms.FileField(
        validators=[file_size, validate_document_file_extension],
        help_text="Only PDF or DOC formats. Maximum file size is 2MiB."
    )
    reference_letter_2 = forms.FileField(
        required=False,
        validators=[file_size, validate_document_file_extension],
        help_text="Only PDF or DOC formats. Maximum file size is 2MiB."
    )

    class Meta:
        model = EmploymentHistory
        fields = ["employer_name", "job_title", "hours_per_week", "reference_letter_1", "reference_letter_2"]
