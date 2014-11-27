from django.contrib import admin
import offer.models


admin.site.register(offer.models.BuyOffer)
admin.site.register(offer.models.SaleOffer)
