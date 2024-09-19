# cmsapi/serializers.py
from rest_framework import serializers
from wagtail.models import Page
from home.models import PostPage  # Import your PostPage model
from base.models import PostType
from taggit.serializers import TagListSerializerField, TaggitSerializer

from rest_framework import serializers
from wagtail.images.models import Image
from wagtail.images.api.fields import ImageRenditionField
from base.models import Video
# # Get the Wagtail image model
# Image = get_image_model()



class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = ['id', 'name']

class ImageSerializer(serializers.ModelSerializer):
    # You can add renditions for various sizes if needed
    url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['url']

    def get_url(self, obj):
        # Get the rendition with the desired size
        rendition = obj.get_rendition('fill-200x200')
        return rendition.url  # Return only the URL of the rendition

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'url', "tags"]  # Add other fields as needed

class PostPageSerializer(TaggitSerializer, serializers.ModelSerializer):
    
    tags = TagListSerializerField(required=False)
    type = TypeSerializer()
    thumbnail = ImageSerializer()
    class Meta:
        model = PostPage
        fields = ['id', 'title', 'slug', 'type', 'tags', 'url','thumbnail', 'search_description', "live"]   # Add any additional fields if necessary
    
class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'url', 'description']  # Add any additional fields if necessary
    
