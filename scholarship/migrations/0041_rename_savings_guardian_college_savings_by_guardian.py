# Generated by Django 4.2.7 on 2023-11-14 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0040_alter_college_applied_for_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='savings_guardian',
            new_name='savings_by_guardian',
        ),
    ]
