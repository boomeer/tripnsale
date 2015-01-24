#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from mail.utils import SendMail
import django
import sys
django.setup()

if __name__ == "__main__":
    print("sending...")
    SendMail(sys.argv[1], "mail/test.html")
