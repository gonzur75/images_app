import os

from config import settings
from ..models import Thumbnail
from django.test import override_settings


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_dir', 'media'))
def test_thumbnail_creation(image_handler, image, remove_test_data):
    image_handler = next(image_handler)
    thumbnail = Thumbnail.objects.create(
        image=image_handler,
        url=image,
        height=42
    )

    assert thumbnail.image == image_handler
    assert thumbnail.url.url == f'/media/resized_images/{image.name}'
    assert thumbnail.height == 42
    assert str(thumbnail) == f'resized_images/{image.name}'
    assert isinstance(thumbnail, Thumbnail)


def test_thumbnail_fields(image_handler, image):
    image_handler = next(image_handler)
    thumbnail = Thumbnail.objects.create(
        image=image_handler,
        url=image,
        height=43
    )
    assert [*vars(thumbnail)] == ['_state', 'id', 'image_id', 'url', 'height']