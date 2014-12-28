#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from place.models import *
from offer.models import *
from user.models import *
import django
from datetime import datetime


if __name__ == "__main__":
    django.setup()
    users = User.objects.all()
    for user in users:
        print(user.fullname())
        user.birthday = datetime.now().date()
        user.save()

