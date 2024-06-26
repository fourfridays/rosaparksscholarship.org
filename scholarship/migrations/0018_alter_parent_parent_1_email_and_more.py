# Generated by Django 4.2.7 on 2023-11-12 14:11

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0017_alter_parent_parent_1_address1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='parent_1_email',
            field=models.EmailField(max_length=254, verbose_name='Parent 1 Email Address'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_1_full_name',
            field=models.CharField(max_length=40, verbose_name='Parent 1 Full Name'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_1_job_title',
            field=models.CharField(max_length=40, verbose_name='Parent 1 Job Title'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_1_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US', verbose_name='Parent 1 Phone Number'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_1_place_of_employment',
            field=models.CharField(max_length=120, verbose_name='Parent 1 Place of Employment'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_1_state',
            field=models.CharField(choices=[('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='MI', max_length=20, verbose_name='Parent 1 State'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_1_zip_code',
            field=models.CharField(max_length=12, verbose_name='Parent 1 Zip Code'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_2_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Parent 2 Email Address'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_2_full_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Parent 2 Full Name'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_2_job_title',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Parent 2 Job Title'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_2_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='US', verbose_name='Parent 2 Phone Number'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_2_place_of_employment',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Parent 2 Place of Employment'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_2_state',
            field=models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='MI', max_length=20, null=True, verbose_name='Parent 2 State'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_2_zip_code',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Parent 2 Zip Code'),
        ),
    ]
