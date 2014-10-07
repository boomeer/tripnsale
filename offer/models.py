from django.db import models
from util.utils import TsExc
import util.models
from datetime import datetime


class TlsMustBeListErr(TsExc):
    pass

class TsMustBePairOfDatesErr(TsExc):
    pass


class Offer(util.models.ContentHolder):
    class Meta:
        abstract = True


class BuyOffer(Offer):
    costFrom = models.FloatField(default=None)
    costTo = models.FloatField(default=None)


class SaleOffer(Offer):
    fr = models.TextField(default="")
    frTime = models.DateTimeField(default=datetime.now())
    to = models.TextField(default="")
    toTime = models.DateTimeField(default=datetime.now())
    deposit = models.FloatField(default=None)

