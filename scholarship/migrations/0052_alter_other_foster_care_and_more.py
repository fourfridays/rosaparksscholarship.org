# Generated by Django 4.2.7 on 2023-12-05 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0051_alter_attachments_reference_letter_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other',
            name='foster_care',
            field=models.BooleanField(default=False, help_text='Are you in the foster care system, or are you an emancipated minor? If so, please indicate yes (This answer does not impact the judging process).'),
        ),
        migrations.AlterField(
            model_name='other',
            name='other_scholarships',
            field=models.TextField(default='', help_text='Other scholarships you have applied for'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='other',
            name='other_scholarships_awarded',
            field=models.TextField(default='', help_text='Scholarships/grants you have already been awarded (name, amount and period of time covered)'),
            preserve_default=False,
        ),
    ]
