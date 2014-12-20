#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from gallery.models import *
from util.utils import GetNewId
import django


if __name__ == "__main__":
    django.setup()
    galleries = Gallery.objects.all()
    for g in galleries:
        if not g.token:
            g.token = GetNewId()
            g.save()
    
