from django.conf.urls import patterns, include, url 
from offer.views import *


urlpatterns = patterns('',
    url("^$", MainView),
    url("^buy/$", BuyOfferAddView),
    url("^sale/$", SaleOfferAddView),
    url("^sale/filter/$", SaleFilterView),
    url("^sale/view/(?P<id>[0-9]{1,})$", SaleView),
)
