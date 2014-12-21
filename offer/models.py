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
    removed = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    createTime = models.DateTimeField(default=datetime.now())

    def visible(self):
        return not self.removed


class BuyOffer(Offer):
    ititle = models.TextField(default="", blank=True)
    costFrom = models.FloatField(default=None)
    costTo = models.FloatField(default=None)
    guarant = models.BooleanField(default=False)
    fr = models.ForeignKey(Country, related_name="buy_country_from", blank=True, null=True)
    frCity = models.TextField(default="", blank=True)
    ifrCity = models.TextField(default="", blank=True)
    to = models.ForeignKey(Country, related_name="buy_country_to", blank=True, null=True)
    toCity = models.TextField(default="", blank=True)
    itoCity = models.TextField(default="", blank=True)
    gallery = models.ForeignKey(Gallery)

@admin.register(BuyOffer)
class BuyOfferAdmin(admin.ModelAdmin):
    list_display = ('costFrom', 'costTo', 'guarant', 'owner', 'closed', 'removed',)


class SaleOffer(Offer):
    fr = models.ForeignKey(Country, related_name="country_from", blank=True, null=True)
    frCity = models.TextField(default="", blank=True)
    ifrCity = models.TextField(default="", blank=True)
    frTime = models.DateTimeField(default=datetime.now())
    to = models.ForeignKey(Country, related_name="country_to", blank=True, null=True)
    toCity = models.TextField(default="", blank=True)
    itoCity = models.TextField(default="", blank=True)
    toTime = models.DateTimeField(default=datetime.now())
    deposit = models.FloatField(default=None)
    guarant = models.BooleanField(default=False)

    def isCurrent(self):
        return self.frTime <= datetime.now() <= self.toTime

    def toEnd(self):
        return self.toTime - datetime.now()

@admin.register(SaleOffer)
class SaleOfferAdmin(admin.ModelAdmin):
    list_display = ("fr", "frCity", "frTime", "to", "toCity", "toTime", "deposit", "guarant",
                "owner")
