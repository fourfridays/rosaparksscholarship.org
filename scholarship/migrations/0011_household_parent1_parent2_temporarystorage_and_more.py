# Generated by Django 4.2.6 on 2023-11-06 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0010_alter_user_id_alter_usersession_id'),
        ('scholarship', '0010_remove_employmenthistory_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_household_income', models.CharField(choices=[('0-20000', '0 - 20000'), ('20000-40000', '20000 - 40000'), ('40000-60000', '40000 - 60000'), ('60000-80000', '60000 - 80000'), ('80000-100000', '80000 - 100000'), ('100000-120000', '100000 - 120000'), ('120000-140000', '120000 - 140000'), ('140000+', '140000+')], max_length=20)),
                ('siblings', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('address1', models.CharField(max_length=35, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address line 2')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='MI', max_length=20)),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US')),
                ('place_of_employment', models.CharField(max_length=120)),
                ('job_title', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Parent 1 Information',
            },
        ),
        migrations.CreateModel(
            name='Parent2',
            fields=[
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('address1', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address line 2')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='MI', max_length=20, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=12, null=True, verbose_name='ZIP')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='US')),
                ('place_of_employment', models.CharField(blank=True, max_length=120, null=True)),
                ('job_title', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Family Information',
            },
        ),
        migrations.CreateModel(
            name='TemporaryStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(max_length=50)),
                ('data', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Temporary Storage',
            },
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='reference_letter_1',
        ),
        migrations.RemoveField(
            model_name='employmenthistory',
            name='reference_letter_2',
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='high_school',
            field=models.CharField(default='None', max_length=120),
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='high_school_city',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.DeleteModel(
            name='FamilyInformation',
        ),
    ]
