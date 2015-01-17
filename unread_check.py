#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from user.utils import CheckUnreadMsgs
import django
import sys


if __name__ == "__main__":
    django.setup()
    CheckUnreadMsgs(hours=12, checkNotified=True)
