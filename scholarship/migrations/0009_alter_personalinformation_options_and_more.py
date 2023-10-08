# Generated by Django 4.2.4 on 2023-10-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0008_personalinformation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalinformation',
            options={'verbose_name_plural': 'Personal Information'},
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='employer_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='parent_1_address1',
            field=models.CharField(max_length=35, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='parent_1_address2',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='parent_1_city',
            field=models.CharField(max_length=30, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='parent_1_job_title',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='parent_2_address1',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='parent_2_address2',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='parent_2_city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='address1',
            field=models.CharField(max_length=35, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='address2',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='city',
            field=models.CharField(max_length=30, verbose_name='City'),
        ),
    ]
