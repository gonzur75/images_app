from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from images import models
from images.models import Image
from images.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(author=user)


class ThumbnailViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):

        thumbnail = models.Thumbnail.objects.create(
            image=models
        )
