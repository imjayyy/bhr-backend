from django.db import models
from django import forms
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import ListBlock, CharBlock
from .blocks import BlogStreamBlock

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

class PostPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', on_delete=models.CASCADE, related_name='tagged_items')


class HomePage(Page):
    # add the Hero section of HomePage:

    parent_page_types = []  # This means it can't be a subpage of any other page

    # Disable any child pages from being added under HomePage
    subpage_types = []  # This means no subpages can be added under HomePage

    
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero section",
        ),
        FieldPanel('body'),
    ]


class PostPage(Page):

    tags = ClusterTaggableManager(through=PostPageTag, blank=True)    
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    body = StreamField(
        BlogStreamBlock(),
        blank=True,
        use_json_field=True,
        help_text="Use this section to write blog content.",
    )
    # type = ParentalManyToManyField("base.PostType", blank=True)
    type = models.ForeignKey(
        "base.PostType",
        on_delete=models.PROTECT,
        help_text="Select a type for this blog post",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('thumbnail'),
        FieldPanel('type'),
        FieldPanel('tags'),
    ]
