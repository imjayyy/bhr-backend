# cmsapi/serializers.py
from rest_framework import serializers
from wagtail.models import Page
from home.models import PostPage  # Import your PostPage model
from base.models import PostType
from taggit.serializers import TagListSerializerField, TaggitSerializer

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'url', "tags"]  # Add other fields as needed

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = ['id', 'name']


class PostPageSerializer(TaggitSerializer, serializers.ModelSerializer):
    
    tags = TagListSerializerField(required=False)
    type = TypeSerializer()
    class Meta:
        model = PostPage
        fields = ['id', 'title', 'slug', 'type', 'tags', 'url']  # Add any additional fields if necessary
    
