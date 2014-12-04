#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from offer.models import *
from gallery.utils import *
import django


if __name__ == "__main__":
    django.setup()
    buys = BuyOffer.objects.all()
    for buy in buys:
        try:
            buy.gallery
        except:
            buy.gallery = CreateGallery()
            buy.save()
