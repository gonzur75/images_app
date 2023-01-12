from django.urls import path

from . import views
from rest_framework.routers import SimpleRouter

app_name = 'images'

router = SimpleRouter()
router.register('images', views.ImageViewSet, basename='images')

urlpatterns = router.urls