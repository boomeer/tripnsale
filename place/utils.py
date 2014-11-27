from place.models import *


def GetCountries():
    return sorted(Country.objects.all(), key=lambda country: country.title)
