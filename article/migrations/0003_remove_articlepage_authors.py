# Generated by Django 4.2.1 on 2023-05-20 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_articlepage_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='authors',
        ),
    ]