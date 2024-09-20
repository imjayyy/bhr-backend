from django.shortcuts import render
from .models import Video
from wagtail.admin.viewsets.model import ModelViewSet

# Create your views here.
class VideoViewSet(ModelViewSet):
    model = Video   
    form_fields = ["url", "title", "thumbnail", "description"]

    icon = "media"
    add_to_admin_menu = True
    copy_view_enabled = False
    inspect_view_enabled = True

