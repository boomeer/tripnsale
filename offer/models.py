from django.db import models
from util.utils import TsExc
import util.models
from django.contrib import admin
from user.models import User
from datetime import datetime
from place.models import (
    Country,
)
from gallery.models import (
    Gallery,
    Photo,
)


class Offer(util.models.ContentHolder):
    class Meta:
        abstract = True
    owner = models.ForeignKey(User, default=None, blank=True, null=True)


class BuyOffer(Offer):
    costFrom = models.FloatField(default=None)
    costTo = models.FloatField(default=None)
    guarant = models.BooleanField(default=False)
    gallery = models.ForeignKey(Gallery)

@admin.register(BuyOffer)
class BuyOfferAdmin(admin.ModelAdmin):
    list_display = ('costFrom', 'costTo', 'guarant', 'owner')


class SaleOffer(Offer):
    fr = models.ForeignKey(Country, related_name="country_from")
    frCity = models.TextField(default="")
    ifrCity = models.TextField(default="")
    frTime = models.DateTimeField(default=datetime.now())
    to = models.ForeignKey(Country, related_name="country_to")
    toCity = models.TextField(default="")
    itoCity = models.TextField(default="")
    toTime = models.DateTimeField(default=datetime.now())
    deposit = models.FloatField(default=None)
    guarant = models.BooleanField(default=False)

@admin.register(SaleOffer)
class SaleOfferAdmin(admin.ModelAdmin):
    list_display = ("fr", "frCity", "frTime", "to", "toCity", "toTime", "deposit", "guarant",
                "owner")
