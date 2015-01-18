#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from mail.utils import SendMail
import django
import sys


if __name__ == "__main__":
    django.setup()
    print("sending...")
    SendMail("info@tripnsale.com", sys.argv[1], "it's dummy")
    
