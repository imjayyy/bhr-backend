from django.core.management.base import BaseCommand
from django.urls import get_resolver, URLPattern, URLResolver

def list_urls(urlpatterns, parent=''):
    """
    Recursively list URLs from a list of patterns
    """
    url_list = []
    for pattern in urlpatterns:
        if isinstance(pattern, URLPattern):
            url_list.append(parent + str(pattern.pattern))
        elif isinstance(pattern, URLResolver):
            url_list += list_urls(pattern.url_patterns, parent + str(pattern.pattern))
    return url_list

class Command(BaseCommand):
    help = "List all URLs in the project"
    def handle(self, *args, **options):
        urls = list_urls(get_resolver().url_patterns)
        for url in urls:
            self.stdout.write(url)
