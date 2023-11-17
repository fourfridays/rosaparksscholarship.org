# Generated by Django 4.2.7 on 2023-11-17 00:05

from django.db import migrations, models
import page.storage_backends
import scholarship.models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0045_alter_attachments_options_attachments_essay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachments',
            name='honors_awards',
            field=models.FileField(default='', help_text='Tell us about the honors and awards you received.\xa0 Indicate whether they were on a local (school, county, or district), state or national level. These awards may be outside of school activities but should not be duplicated in any other section.', storage=page.storage_backends.PrivateMediaStorage(), upload_to=scholarship.models.get_user_file_path_honors_awards),
            preserve_default=False,
        ),
    ]
