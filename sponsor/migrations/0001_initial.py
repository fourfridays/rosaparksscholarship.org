# Generated by Django 4.2.4 on 2023-08-06 17:52

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('sponsor', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=100)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.URLBlock())], icon='image'))], default='', use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
