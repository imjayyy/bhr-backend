# cmsapi/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageViewSet, PostPageViewSet, PostTypeViewSet, ApiDocView, VideoViewSet

router = DefaultRouter()
# router.register('list', ApiDocView)
router.register(r'pages', PageViewSet)
router.register(r'postpages', PostPageViewSet)  # Register your viewset
router.register(r'posttypes', PostTypeViewSet)  # Register PostTypeViewSet
router.register(r'videos', VideoViewSet)  # Register PostTypeViewSet


urlpatterns = [
    path('', include(router.urls)),
    path('api-doc/', ApiDocView, name='api-doc'),  # Add the view to your URLs

    
]
