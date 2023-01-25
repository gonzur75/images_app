import os
import shutil

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings

from config import settings
from config.settings import BASE_DIR
from images.models import Image


@pytest.fixture
def user(db, django_user_model):
    return django_user_model.objects.create_user(
        username='testuser',
        password='testPass123'
    )


@pytest.fixture
@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_dir', 'media'))
def image_handler(db, user):
    image = Image.objects.create(
        author=user,
        url=SimpleUploadedFile('test_file.jpg', content=open(os.path.join('tests', 'test_image.jpg'), 'rb').read())
    )

    yield image
    # os.remove(os.path.join(BASE_DIR, 'media', 'images', 'test_file.jpg'))


@pytest.fixture
def image():
    yield SimpleUploadedFile('test_file.jpg', content=open(os.path.join('tests', 'test_image.jpg'), 'rb').read())


@pytest.fixture
def remove_test_data():
    yield shutil.rmtree(os.path.join(settings.BASE_DIR, 'test_dir'), ignore_errors=True)
