# Generated by Django 4.2.4 on 2023-09-24 18:49

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_judge_user_is_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='6305440234', max_length=128, region='US'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_judge',
            field=models.BooleanField(default=False, verbose_name='is judge'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=True, verbose_name='is student'),
        ),
    ]
