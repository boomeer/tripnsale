#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
import util.valute


if __name__ == "__main__":
    util.valute.UpdateRates()
