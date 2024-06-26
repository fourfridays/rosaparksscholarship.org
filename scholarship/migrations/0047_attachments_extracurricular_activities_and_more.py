# Generated by Django 4.2.7 on 2023-11-17 00:16

from django.db import migrations, models
import page.storage_backends
import scholarship.models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0046_attachments_honors_awards'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachments',
            name='extracurricular_activities',
            field=models.FileField(default='', storage=page.storage_backends.PrivateMediaStorage(), upload_to=scholarship.models.get_user_file_path_extracurricular_activities),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attachments',
            name='honors_awards',
            field=models.FileField(storage=page.storage_backends.PrivateMediaStorage(), upload_to=scholarship.models.get_user_file_path_honors_awards),
        ),
    ]
