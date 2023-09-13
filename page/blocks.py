from wagtail.admin.panels import FieldPanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    DateBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
)
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtailcodeblock.blocks import CodeBlock

COLOR_PRIMARY = "primary"
COLOR_SECONDARY = "secondary"
COLOR_TERTIARY = "tertiary"
COLOR_SUCCESS = "success"
COLOR_DANGER = "danger"
COLOR_WARNING = "warning"
COLOR_INFO = "info"
COLOR_LIGHT = "light"
COLOR_DARK = "dark"

COLOR_CHOICES = (
    (COLOR_PRIMARY, "Primary"),
    (COLOR_SECONDARY, "Secondary"),
    (COLOR_TERTIARY, "Tertiary"),
    (COLOR_SUCCESS, "Success"),
    (COLOR_DANGER, "Danger"),
    (COLOR_WARNING, "Warning"),
    (COLOR_INFO, "Info"),
    (COLOR_LIGHT, "Light"),
    (COLOR_DARK, "Dark"),
)


class AlignmentBlock(ChoiceBlock):
    choices = [("start", "Left"), ("center", "Center"), ("end", "Right")]


class VerticalAlignmentBlock(ChoiceBlock):
    choices = [("start", "Left"), ("center", "Center"), ("end", "Right")]


class ButtonBlock(StructBlock):
    alignment = AlignmentBlock(default="start")
    size = ChoiceBlock([("sm", "Small"), ("md", "Medium"), ("lg", "Large")])
    cta_text = CharBlock(max_length=25, help_text="25 character limit.")
    internal_link = PageChooserBlock(required=False)
    external_link = URLBlock(required=False)
    color = ChoiceBlock(
        choices=COLOR_CHOICES,
    )

    class Meta:
        icon = "pick"
        template = "blocks/button_block.html"


class CodeBlock(StructBlock):
    code = CodeBlock(label="Code")


class DocumentBlock(StructBlock):
    document = DocumentChooserBlock(required=False)

    class Meta:
        icon = "doc-full"
        template = "blocks/document_block.html"


class HeroImageBlock(StructBlock):
    hero_image = ImageChooserBlock(required=True)
    hero_heading = CharBlock(
        required=False, max_length=40, help_text="40 character limit."
    )
    hero_message = CharBlock(
        required=False, max_length=240, help_text="240 character limit."
    )
    hero_cta = CharBlock(
        required=False,
        verbose_name="Hero CTA",
        max_length=20,
        help_text="Text to display on Call to Action. 20 character limit.",
    )

    class Meta:
        icon = "image"
        template = "blocks/hero_image_block.html"


class PersonDateBlock(StructBlock):
    date = DateBlock(required=False)
    people = StreamBlock(
        [
            ("person", SnippetChooserBlock("page.People")),
        ]
    )

    panels = [
        # Use a SnippetChooserPanel because article.ArticleAuthor is registered as a snippet
        FieldPanel("people"),
    ]


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alignment = AlignmentBlock(default="start", required=False)
    border = BooleanBlock(required=False, help_text="Adds border around image")

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class ImageGridBlock(StreamBlock):
    grid = StructBlock(
        [
            ("image", ImageChooserBlock(required=True, help_text="size: 800X450px")),
            ("caption", CharBlock(max_length=26, help_text="26 characters limit")),
            (
                "description",
                CharBlock(
                    max_length=300, required=False, help_text="300 characters limit"
                ),
            ),
            ("internal_link", PageChooserBlock(required=False)),
            ("external_link", URLBlock(required=False)),
        ]
    )

    class Meta:
        icon = "image"
        template = "blocks/image_grid_block.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    paragraph_block = RichTextBlock(
        features=[
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "bold",
            "italic",
            "link",
            "code",
            "ul",
            "ol",
            "strikethrough",
            "superscript",
            "subscript",
        ],
        icon="pilcrow",
        template="blocks/paragraph_block.html",
    )
    image_block = ImageBlock()
    button_block = ButtonBlock()
    image_grid_block = ImageGridBlock()
    document_block = DocumentBlock()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks",
        icon="code",
        template="blocks/embed_block.html",
    )
    table = TableBlock(template="includes/table.html")
    code_block = CodeBlock()


class SingleColumnBlock(StructBlock):
    column = BaseStreamBlock()
    alignment = AlignmentBlock(default="start", required=False)
    vertical_alignment = VerticalAlignmentBlock(required=False)

    class Meta:
        label = "Single Column"
        template = "blocks/single_column_block.html"


class TwoColumnBlock(StructBlock):
    left_column = BaseStreamBlock()
    right_column = BaseStreamBlock()
    alignment = AlignmentBlock(default="start", required=False)
    vertical_alignment = VerticalAlignmentBlock(required=False)

    class Meta:
        label = "Two Columns"
        template = "blocks/two_column_block.html"


class ThreeColumnBlock(StructBlock):
    left_column = BaseStreamBlock()
    middle_column = BaseStreamBlock()
    right_column = BaseStreamBlock()
    alignment = AlignmentBlock(default="start", required=False)
    vertical_alignment = VerticalAlignmentBlock(required=False)

    class Meta:
        label = "Three Columns"
        template = "blocks/three_column_block.html"


class FourColumnBlock(StructBlock):
    left_column_1 = BaseStreamBlock()
    left_column_2 = BaseStreamBlock()
    right_column_1 = BaseStreamBlock()
    right_column_2 = BaseStreamBlock()
    alignment = AlignmentBlock(default="start", requirement=False)
    vertical_alignment = VerticalAlignmentBlock(required=False)

    class Meta:
        label = "Four Columns"
        template = "blocks/four_column_block.html"


class SponsorBlock(StructBlock):
    name = CharBlock(max_length=100)
    image = ImageChooserBlock()
    link = URLBlock()

    class Meta:
        label = "Sponsor Block"
        template = "blocks/sponsor_block.html"
