from django.db import models
from util.utils import TsExc
import util.models
from user.models import User
from datetime import datetime


class Country(models.Model):
    title = models.TextField(default="")
    name = models.TextField(default="")
    
    
class Offer(util.models.ContentHolder):
    class Meta:
        abstract = True
    owner = models.ForeignKey(User, default=None, blank=True, null=True)


class BuyOffer(Offer):
    costFrom = models.FloatField(default=None)
    costTo = models.FloatField(default=None)
    guarant = models.BooleanField(default=False)


class SaleOffer(Offer):
    fr = models.ForeignKey(Country, related_name="country_from")
    frCity = models.TextField(default="")
    frTime = models.DateTimeField(default=datetime.now())
    to = models.ForeignKey(Country, related_name="country_to")
    toCity = models.TextField(default="")
    toTime = models.DateTimeField(default=datetime.now())
    deposit = models.FloatField(default=None)
    guarant = models.BooleanField(default=False)
