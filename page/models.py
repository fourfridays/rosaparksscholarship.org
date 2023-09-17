from django.conf import settings
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from page.blocks import ImageGridBlock, SingleColumnBlock, TwoColumnBlock, ThreeColumnBlock, FourColumnBlock, HeroImageBlock


class HomePage(Page):
    pass

    # Restricting the creation of this page type in settings
    is_creatable = settings.WAGTAIL_PAGES_IS_CREATABLE

    # Restricting the page from being created anywhere other than root
    parent_page_types = ['wagtailcore.Page']


class StandardPage(Page):
    body = StreamField([
        ('hero_image', HeroImageBlock(icon='image')),
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('image_grid', ImageGridBlock(icon='image', min_num=2, max_num=4, help_text='Minimum 2 blocks and a maximum of 4 blocks')),
    ], use_json_field=True, default='')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
