from django.db import models
from util.utils import TsExc
import util.models
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

    def __init__(self, *args, **argv):
        super().__init__(*args, **argv)
        if self.toTime.date() < datetime.now().date():
            self.closed = True

    def isCurrent(self):
        return self.frTime.date() <= datetime.now().date() <= self.toTime.date()

    def toEnd(self):
        return self.toTime - datetime.now()

class AbstractRecommendVisit(util.models.ContentHolder):
    class Meta:
        abstract = True

    EMAIL = "M"
    VISITED = "V"
    VISIT_TYPE = (
        (EMAIL, "email",),
        (VISITED, "visited",),
    )
    visType = models.CharField(max_length=1,
                               choices=VISIT_TYPE,
                               default=VISITED)
    user = models.ForeignKey(User)
    time = models.DateTimeField(default=datetime.now())

class SaleRecommendVisit(AbstractRecommendVisit):
    baseOffer = models.ForeignKey(SaleOffer)
    recOffer = models.ForeignKey(BuyOffer)

    def __init__(self, *args, **argv):
        super().__init__(*args, **argv)

class BuyRecommendVisit(AbstractRecommendVisit):
    baseOffer = models.ForeignKey(BuyOffer)
    recOffer = models.ForeignKey(SaleOffer)

    def __init__(self, *args, **argv):
        super().__init__(*args, **argv)

class OfferConnection(models.Model):
    user = models.ForeignKey(User)
    buy = models.ForeignKey(BuyOffer, null=True, blank=True)
    sale = models.ForeignKey(SaleOffer, null=True, blank=True)
