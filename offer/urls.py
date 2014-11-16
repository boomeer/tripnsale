from django.conf.urls import patterns, include, url 
from offer.views import *


urlpatterns = patterns('',
    url("^buy/$", BuyOfferAddView),
    url("^buy/filter/$", BuyFilterView),
    url("^buy/view/(?P<id>[0-9]{1,})$", BuyView),
    url("^buy/list/$", BuyListView),
    url("^sale/$", SaleOfferAddView),
    url("^sale/filter/$", SaleFilterView),
    url("^sale/view/(?P<id>[0-9]{1,})$", SaleView),
    url("^sale/list/$", SaleListView),
)
