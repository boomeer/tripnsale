#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tripnsale.settings")
from place.models import *
from offer.models import *
import django


if __name__ == "__main__":
    django.setup()
    sales = SaleOffer.objects.all()
    for sale in sales:
        sale.itoCity = sale.toCity.lower()
        sale.ifrCity = sale.frCity.lower()
        sale.save()
    countries = Country.objects.all()
    for country in countries:
        country.ititle = country.title.lower()
        country.save()
    
