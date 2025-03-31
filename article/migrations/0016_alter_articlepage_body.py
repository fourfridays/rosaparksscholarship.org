# Generated by Django 5.0.9 on 2025-03-31 19:52

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_alter_articlepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph_block', 0), ('image_block', 5), ('button_block', 12), ('image_grid_block', 17), ('document_block', 19), ('embed_block', 20), ('table', 21), ('code_block', 25)], blank=True, block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {'features': ['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'code', 'ul', 'ol', 'strikethrough', 'superscript', 'subscript'], 'icon': 'pilcrow', 'template': 'blocks/paragraph_block.html'}), 1: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 2: ('wagtail.blocks.CharBlock', (), {'required': False}), 3: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('start', 'Left'), ('center', 'Center'), ('end', 'Right')], 'required': False}), 4: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('none', 'None'), ('thumbnail', 'Thumbnail'), ('rounded-circle', 'Rounded Circle')], 'help_text': 'Select the image border style', 'label': 'Image Border'}), 5: ('wagtail.blocks.StructBlock', [[('image', 1), ('caption', 2), ('attribution', 2), ('alignment', 3), ('border', 4)]], {}), 6: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('start', 'Left'), ('center', 'Center'), ('end', 'Right')]}), 7: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')]}), 8: ('wagtail.blocks.CharBlock', (), {'help_text': '25 character limit.', 'max_length': 25}), 9: ('wagtail.blocks.PageChooserBlock', (), {'required': False}), 10: ('wagtail.blocks.URLBlock', (), {'required': False}), 11: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('none', 'None'), ('light', 'Light'), ('secondary', 'Secondary')]}), 12: ('wagtail.blocks.StructBlock', [[('alignment', 6), ('size', 7), ('cta_text', 8), ('internal_link', 9), ('external_link', 10), ('color', 11)]], {}), 13: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Image size set to max : 400X225px', 'required': True}), 14: ('wagtail.blocks.CharBlock', (), {'help_text': '26 characters limit', 'max_length': 26}), 15: ('wagtail.blocks.CharBlock', (), {'help_text': '300 characters limit', 'max_length': 300, 'required': False}), 16: ('wagtail.blocks.StructBlock', [[('image', 13), ('caption', 14), ('description', 15), ('internal_link', 9), ('external_link', 10)]], {}), 17: ('wagtail.blocks.StreamBlock', [[('grid', 16)]], {}), 18: ('wagtail.documents.blocks.DocumentChooserBlock', (), {'required': False}), 19: ('wagtail.blocks.StructBlock', [[('document', 18)]], {}), 20: ('wagtail.embeds.blocks.EmbedBlock', (), {'help_text': 'Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', 'icon': 'code', 'max_height': 400, 'max_width': 800, 'template': 'blocks/embed_block.html'}), 21: ('wagtail.contrib.table_block.blocks.TableBlock', (), {'template': 'includes/table.html'}), 22: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], 'help_text': 'Coding language', 'identifier': 'language', 'label': 'Language'}), 23: ('wagtail.blocks.TextBlock', (), {'identifier': 'code', 'label': 'Code'}), 24: ('wagtail.blocks.StructBlock', [[('language', 22), ('code', 23)]], {'label': 'Code'}), 25: ('wagtail.blocks.StructBlock', [[('code', 24)]], {})}, verbose_name='Article body'),
        ),
    ]
