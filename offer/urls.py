from django.conf.urls import patterns, include, url 
from offer.views import *


urlpatterns = patterns('',
    url("^$", MainView),
    url("^buy/$", BuyOfferAddView),
    url("^sale/$", SaleOfferAddView),
)
