# Generated by Django 4.2.7 on 2023-12-17 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0054_alter_applicationstate_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academiccounselor',
            name='submission_time',
        ),
        migrations.RemoveField(
            model_name='college',
            name='submission_time',
        ),
        migrations.RemoveField(
            model_name='currentemployment',
            name='submission_time',
        ),
        migrations.RemoveField(
            model_name='highschool',
            name='submission_time',
        ),
        migrations.RemoveField(
            model_name='household',
            name='submission_time',
        ),
        migrations.RemoveField(
            model_name='other',
            name='submission_time',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='submission_time',
        ),
        migrations.RemoveField(
            model_name='personalinformation',
            name='submission_time',
        ),
    ]
