# Generated by Django 4.2.7 on 2023-11-12 01:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarship', '0013_alter_personalinformation_state'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmploymentHistory',
            new_name='StudentEmploymentHistory',
        ),
    ]