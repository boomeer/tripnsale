#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
import util.country


if __name__ == "__main__":
    util.country.Main()
