#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from gallery.models import *
from user.models import *
from gallery.utils import *
import django


if __name__ == "__main__":
    django.setup()
    photos = Photo.objects.all()
    for photo in photos:
        if photo.img and not photo.thumbnail:
            MakeThumbnail(photo.img, photo.thumbnail)
            photo.save()
    users = User.objects.all()
    for user in users:
        if user.avatar and not user.avatarThumb:
            MakeThumbnail(user.avatar, user.avatarThumb)
            user.save()
