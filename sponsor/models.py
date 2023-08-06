from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from page.blocks import HeroImageBlock, SponsorBlock


class SponsorPage(Page):
    body = StreamField([
        ('hero_image', HeroImageBlock(icon='image')),
        ('sponsor', SponsorBlock(icon='image')),
    ], use_json_field=True, default='')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
