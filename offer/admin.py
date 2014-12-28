from django.contrib import admin
from offer.models import *


@admin.register(BuyOffer)
class BuyOfferAdmin(admin.ModelAdmin):
    list_display = ('costFrom', 'costTo', 'guarant', 'owner', 'closed', 'removed',)


@admin.register(SaleOffer)
class SaleOfferAdmin(admin.ModelAdmin):
    list_display = ("fr", "frCity", "frTime", "to", "toCity", "toTime", "deposit", "guarant",
                "owner", "closed",)


@admin.register(OfferConnection)
class OfferConnectionAdmin(admin.ModelAdmin):
    list_display = ("user", "buy", "sale",)
