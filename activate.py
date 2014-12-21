#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from util.utils import GetNewId
from user.models import User
from user.utils import SendActivateMail
import django


if __name__ == "__main__":
    django.setup()
    user = User.objects.get(username="ilya.krvn@gmail.com")
    SendActivateMail(user)
    
