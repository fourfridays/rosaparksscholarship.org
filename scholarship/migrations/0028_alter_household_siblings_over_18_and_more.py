# Generated by Django 4.2.7 on 2023-11-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0027_extracurricular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='siblings_over_18',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='siblings_under_18',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]