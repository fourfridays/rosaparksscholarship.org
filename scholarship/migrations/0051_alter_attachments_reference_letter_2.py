# Generated by Django 4.2.7 on 2023-11-30 21:53

from django.db import migrations, models
import page.storage_backends
import scholarship.models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0050_academiccounselor_submission_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='reference_letter_2',
            field=models.FileField(default='', storage=page.storage_backends.PrivateMediaStorage(), upload_to=scholarship.models.get_user_file_path_for_reference_letter_2),
            preserve_default=False,
        ),
    ]
