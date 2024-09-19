from django.db import models
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.fields import RichTextField

# import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin:
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)

# import register_snippet:
from wagtail.snippets.models import register_snippet
from wagtail.models import Page, ClusterableModel
from wagtail.admin.forms.models import WagtailAdminModelForm

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

@register_setting
class NavigationSettings(BaseGenericSetting):
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    mastodon_url = models.URLField(verbose_name="Mastodon URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
            ],
            "Social settings",
        )
    ]

# @register_snippet
# class FooterText(
#     DraftStateMixin,
#     RevisionMixin,
#     PreviewableMixin,
#     TranslatableMixin,
#     models.Model,
# ):

#     body = RichTextField()

#     panels = [
#         FieldPanel("body"),
#         PublishingPanel(),
#     ]

#     def __str__(self):
#         return "Footer text"

#     def get_preview_template(self, request, mode_name):
#         return "base.html"

#     def get_preview_context(self, request, mode_name):
#         return {"footer_text": self.body}

#     class Meta(TranslatableMixin.Meta):
#         verbose_name_plural = "Footer Text"


class PostType(
    # DraftStateMixin,
    # PreviewableMixin,
    # RevisionMixin,
    # TranslatableMixin,
    models.Model):

    """Post Type for a snippet"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name='Slug', 
        allow_unicode=True, 
        max_length=255, 
        help_text='A slug to identify type')
    
    panels = [
        FieldPanel('name'),
        FieldPanel('slug')
    ]

    class Meta:
        verbose_name = "Post Type"
        ordering = ['name']

    def __str__(self):
        return self.name
    
register_snippet(PostType)


class VideoTag(TaggedItemBase):
    content_object = ParentalKey('Video', on_delete=models.CASCADE, related_name='video_tagged_items')

class Video(ClusterableModel, models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = ClusterTaggableManager(through=VideoTag, blank=True)

    def __str__(self) -> str:
        return self.title

    # Add other fields as needed


# class VideoForm(WagtailAdminModelForm):
#     class Meta:
#         model = Video





