from offer.models import *
from util.utils import (
    ValidFilter,
    TsExc,
)
from django.template.loader import render_to_string
from mail.utils import SendMail
import tripnsale.settings as settings


def CheckConnection(user, offer):
    oc = OfferConnection.objects.filter(user=user)
    if type(offer) == BuyOffer:
        oc = oc.filter(buy=offer)
    elif type(offer) == SaleOffer:
        oc = oc.filter(sale=offer)
    else:
        raise TsExc("bad_offer_type")
    return not oc.count()


def SendOfferMail(user, offer, conf):
    if type(offer) == BuyOffer:
        content = render_to_string("mail/buy_offer.html", {
            "user": user,
            "buy": offer,
            "conf": conf,
            "hostAddr": settings.CURRENT_HOST,
        })
    elif type(offer) == SaleOffer:
        content = render_to_string("mail/sale_offer.html", {
            "user": user,
            "sale": offer,
            "conf": conf,
            "hostAddr": settings.CURRENT_HOST,
        })
    else:
        raise TsExc("bad_offer_type")
    SendMail("info@tripnsale.com", offer.owner.email, content)

class SaleEditErr (TsExc):
    def __init__(self, msg):
        super().__init__(msg)
        self.status = msg

class SaleFrDateMissingErr (SaleEditErr):
    def __init__(self):
        super().__init__("fromdate_is_empty")

class SaleFrDateInvalidErr (SaleEditErr):
    def __init__(self):
        super().__init__("fromdate_is_invalid")

class SaleFrCountryMissingErr (SaleEditErr):
    def __init__(self):
        super().__init__("fromcountry_is_empty")

class SaleFrCountryInvalidErr (SaleEditErr):
    def __init__(self):
        super().__init__("fromcountry_is_invalid")

class SaleToDateMissingErr (SaleEditErr):
    def __init__(self):
        super().__init__("todate_is_empty")

class SaleToDateInvalidErr (SaleEditErr):
    def __init__(self):
        super().__init__("todate_is_invalid")

class SaleBadDatesRelations (SaleEditErr):
    def __init__(self):
        super().__init__("bad_date_relations")

class SaleToCountryMissingErr (SaleEditErr):
    def __init__(self):
        super().__init__("tocountry_is_empty")

class SaleToCountryInvalidErr (SaleEditErr):
    def __init__(self):
        super().__init__("tocountry_is_invalid")

class SaleInvalidDepositErr (SaleEditErr):
    def __init__(self):
        super().__init__("invalid_deposit")

def ExtractSaleFields(params):
    if not params.get("from", "").strip():
        raise SaleFrCountryMissingErr
    try:
        fr = Country.objects.get(name=params["from"])
    except ValueError:
        raise SaleFrCountryInvalidErr

    if not params.get("to", "").strip():
        raise SaleToCountryMissingErr
    try:
        to = Country.objects.get(name=params["to"])
    except ValueError:
        raise SaleToCountryInvalidErr

    if not params.get("fromTime", "").strip():
        raise SaleFrDateMissingErr
    try:
        frTime = datetime.strptime(params["fromTime"], "%d.%m.%Y")
    except ValueError:
        raise SaleFrDateInvalidErr

    if not params.get("toTime", "").strip():
        raise SaleToDateMissingErr
    try:
        toTime = datetime.strptime(params["toTime"], "%d.%m.%Y")
    except ValueError:
        raise SaleToDateInvalidErr

    if frTime > toTime:
        raise SaleBadDatesRelations

    try:
        deposit = round(float(params.get("deposit", "0").replace(",", ".").strip()))
    except ValueError:
        raise SaleInvalidDepositErr
    if deposit < 0:
        raise SaleInvalidDepositErr

    return (fr, to, frTime, toTime, deposit,)

def SaleFilterExtractParams(request, static=False):
    params = request.REQUEST
    owner = int(params.get("owner", 0))
    sales = SaleOffer.objects
    if owner:
        sales = sales.filter(owner__id=owner)
    sales = sales.all()
    sales = [sale for sale in sales if ValidFilter(sale.fr.title + " " + sale.frCity,
                                                    params.get("from", "")) \
                and ValidFilter(sale.to.title + " " + sale.toCity, params.get("to", ""))]
    sales = [sale for sale in sales if sale.visible()]
    sales = sorted(sales, key=lambda sale: (sale.closed, -sale.isCurrent(), sale.toEnd(),))

    count = max(0, int(params.get("count", 15)))
    totalpages = (len(sales) + count - 1) // count
    page = max(1, min(int(params.get("page", 1)), totalpages)) - 1
    block = sales[page*count:(page+1)*count]
    return {
        "sales": sales,
        "saleblock": block,
        "page": page,
        "totalpages": totalpages,
        "profile": int(params.get("profile", 0)),
        "pagesid": "trips" if not static else "#",
        "static": static,
    }


class BuyEditErr (TsExc):
    def __init__(self, msg):
        super().__init__(msg)
        self.status = msg

class BuyTitleMissingErr (BuyEditErr):
    def __init__(self):
        super().__init__("title_is_missing")

class BuyFrCountryInvalidErr (BuyEditErr):
    def __init__(self):
        super().__init__("fromcountry_is_invalid")

class BuyToCountryMissingErr (BuyEditErr):
    def __init__(self):
        super().__init__("tocountry_is_empty")

class BuyToCountryInvalidErr (BuyEditErr):
    def __init__(self):
        super().__init__("tocountry_is_invalid")

class BuyCostFrInvalidErr (BuyEditErr):
    def __init__(self):
        super().__init__("costfr_is_invalid")

class BuyCostToMissingErr (BuyEditErr):
    def __init__(self):
        super().__init__("costto_is_missing")

class BuyCostToInvalidErr (BuyEditErr):
    def __init__(self):
        super().__init__("costto_is_invalid")

class BuyBadCostRelations (BuyEditErr):
    def __init__(self):
        super().__init__("bad_cost_relations")

def ExtractBuyFields(params):
    if not params.get("from", "").strip():
        fr = None
    else:
        try:
            fr = Country.objects.get(name=params["from"])
        except ValueError:
            raise BuyFrCountryInvalidErr

    if not params.get("to", "").strip():
        raise BuyToCountryMissingErr
    try:
        to = Country.objects.get(name=params["to"])
    except ValueError:
        raise BuyToCountryInvalidErr

    if not params.get("title", "").strip():
        raise BuyTitleMissingErr
    title = params["title"]

    try:
        if not params.get("costFrom", ""):
            costFrom = 0.0
        else:
            costFrom = round(float(params.get("costFrom", "0").replace(",", ".").strip()))
        if costFrom < 0:
            raise ValueError
    except ValueError:
        raise BuyCostFrInvalidErr

    try:
        if not params.get("costTo", "").strip():
            raise BuyCostToMissingErr
        else:
            costTo = round(float(params.get("costTo", "0").replace(",", ".").strip()))
        if costTo < 0:
            raise ValueError
    except ValueError:
        raise BuyCostToInvalidErr

    if costFrom > costTo:
        raise BuyBadCostRelations

    return (fr, to, title, costFrom, costTo,)

def BuyFilterExtractParams(request, static=False):
    params = request.REQUEST
    owner = int(params.get("owner", 0))
    buys = BuyOffer.objects
    if owner:
        buys = buys.filter(owner__id=owner)
    buys = buys.all()
    buys = [buy for buy in buys if ValidFilter(buy.title + " " + buy.content,
                params.get("title", "")) and ValidFilter((buy.fr.title if buy.fr else "") + " " + buy.frCity,
                params.get("fr", "")) \
                and ValidFilter((buy.to.title if buy.to else "") + " " + buy.toCity, params.get("to", ""))]
    buys = [buy for buy in buys if buy.visible()]
    buys = sorted(buys, key=lambda buy: (buy.closed, -buy.id,))
    count = max(0, int(params.get("count", 15)))
    totalpages = (len(buys) + count - 1) // count
    page = max(1, min(int(params.get("page", 1)), totalpages)) - 1
    block = buys[page*count:(page+1)*count]
    return {
        "buys": buys,
        "buyblock": block,
        "page": page,
        "static": static,
        "totalpages": totalpages,
        "profile": int(params.get("profile", 0)),
        "pagesid": "buys" if not static else "#",
    }


