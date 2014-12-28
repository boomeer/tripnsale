#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
import util.country
import django


if __name__ == "__main__":
    django.setup()
    util.country.Main()
