# Generated by Django 4.2.6 on 2023-10-22 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarship', '0009_alter_personalinformation_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employmenthistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='familyinformation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='personalinformation',
            name='id',
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='familyinformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
