# Generated by Django 4.2.7 on 2023-11-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_delete_usersession'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_submitted_attachments',
            field=models.BooleanField(default=False, verbose_name='has submitted attachments'),
        ),
    ]
