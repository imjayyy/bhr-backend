from django.shortcuts import render

# Create your views here.
# cmsapi/views.py
from rest_framework import viewsets
from wagtail.models import Page
from base.models import PostType

from home.models import PostPage
from .serializers import PageSerializer, PostPageSerializer, TypeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.urls import get_resolver, URLPattern, URLResolver

from urllib.parse import urlparse, urlunparse

def clean_url(url):
    # parsed_url = urlparse(request.build_absolute_uri())  # Get the full URL
    # clean_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path  # Rebuild without query parameters
    url = url.rstrip('/')  # Remove trailing slashes
    url = url.replace('^', '')  # Remove the starting caret (^) for regex
    url = url.replace('$', '')  # Remove the ending dollar sign ($) for regex
    url = url.replace('(?P<', '<').replace('>[a-z0-9]+)', '')  # Clean named regex groups
    return url

def list_urls(urlpatterns, parent=''):
    """
    Recursively list URLs from a list of patterns
    """
    url_list = []
    for pattern in urlpatterns:
        if isinstance(pattern, URLPattern):
            cleaned_url = clean_url(parent + str(pattern.pattern))
            url_list.append(cleaned_url)
        elif isinstance(pattern, URLResolver):
            url_list += list_urls(pattern.url_patterns, parent + str(pattern.pattern))
    return url_list
    # help = "List all URLs in the project"
    # def handle(self, *args, **options):
    #     urls = list_urls(get_resolver().url_patterns)
    #     for url in urls:
    #         self.stdout.write(url)


def ApiDocView(request):
    help_text = "List all URLs in the project"

    urls = list_urls(get_resolver().url_patterns)

    response_content = f"<h1>{help_text}</h1><ul>"
    for url in urls:
        if url.startswith('auth') or url.startswith('api'):
            # url = clean_url(url)
            response_content += f"<a href={'http://' + request.get_host()+ '/' + url}><li>{url}</li> </a>"
    response_content += "</ul>"


    return HttpResponse(response_content)


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PostPageViewSet(viewsets.ModelViewSet):
    queryset = PostPage.objects.all()
    serializer_class = PostPageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']  # Enable filtering by 'type'
    queryset = PostPage.objects.all()
    serializer_class = PostPageSerializer


class PostTypeViewSet(viewsets.ModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = TypeSerializer


