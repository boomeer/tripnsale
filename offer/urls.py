from django.conf.urls import patterns, include, url 
from offer.views import *


urlpatterns = patterns('',
    url("^buy/$", BuyOfferAddView),
    url("^buy/filter/$", BuyFilterView),
    url("^buy/view/(?P<id>[0-9]{1,})$", BuyView),
    url("^buy/edit/(?P<id>[0-9]{1,})$", BuyEditView),
    url("^buy/list/$", BuyListView),
    url("^buy/remove/$", BuyRemoveView),
    url("^buy/close/$", BuyCloseView),
    url("^sale/$", SaleOfferAddView),
    url("^sale/filter/$", SaleFilterView),
    url("^sale/view/(?P<id>[0-9]{1,})$", SaleView),
    url("^sale/list/$", SaleListView),
    url("^sale/remove/$", SaleRemoveView),
    url("^sale/close/$", SaleCloseView),
)
