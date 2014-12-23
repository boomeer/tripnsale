from offer.models import *
from util.utils import TsExc
from django.template.loader import render_to_string
from mail.utils import SendMail


def CheckConnection(user, offer):
    oc = OfferConnection.objects.filter(user=user)
    if type(offer) == BuyOffer:
        oc = oc.filter(buy=offer)
    elif type(offer) == SaleOffer:
        oc = oc.filter(sale=offer)
    else:
        raise TsExc("bad_offer_type")
    return not oc.count()


def SendOfferMail(user, offer):
    if type(offer) == BuyOffer:
        content = render_to_string("mail/buy_offer.html", {
            "user": user,
            "buy": offer,
        })
    elif type(offer) == SaleOffer:
        content = render_to_string("mail/sale_offer.html", {
            "user": user,
            "sale": offer,
        })
    else:
        raise TsExc("bad_offer_type")
    SendMail("info@tripnsale.com", offer.owner.email, content)
