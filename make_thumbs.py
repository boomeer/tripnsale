#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from gallery.models import *
from gallery.utils import *
import django


if __name__ == "__main__":
    django.setup()
    photos = Photo.objects.all()
    for photo in photos:
        MakeThumbnail(photo.img, photo.thumbnail)
        photo.save()
