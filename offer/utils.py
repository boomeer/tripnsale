from offer.models import *
from util.utils import (
    ValidFilter,
    TsExc,
    GetCurrentUser,
)
from util.exc import (
    RedirectExc,
)
from django.template.loader import render_to_string
from mail.utils import SendMail
import tripnsale.settings as settings
import collections
from datetime import datetime, timedelta

Recommend = collections.namedtuple('Recommend', ['new', 'rank', 'offer'])

def CheckConnection(user, offer):
    oc = OfferConnection.objects.filter(user=user)
    if type(offer) == BuyOffer:
        oc = oc.filter(buy=offer)
    elif type(offer) == SaleOffer:
        oc = oc.filter(sale=offer)
    else:
        raise TsExc("bad_offer_type")
    return not oc.count()


def SendOfferMail(peer, offer, conf):
    if not offer.owner.emailNotify:
        return

    if type(offer) == BuyOffer:
        SendMail(offer.owner.email, "mail/buy_offer.html", {
            "user": offer.owner,
            "peer": peer,
            "buy": offer,
            "conf": conf,
        })
    elif type(offer) == SaleOffer:
        SendMail(offer.owner.email, "mail/send_offer.html", {
            "user": offer.owner,
            "peer": peer,
            "sale": offer,
            "conf": conf,
        })
    else:
        raise TsExc("bad_offer_type")


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

def _SaleExtractList(params):
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
    return sales

def SaleExtractRecommend(buy, user=None, limit=None):
    sales = SaleOffer.objects.filter(fr__id=buy.to.id)
    sales = sales.exclude(owner__id=buy.owner.id)
    sales = sales.all()

    visits = BuyRecommendVisit.objects
    if user:
        visits = visits.filter(user__id=user.id)
    else:
        visits = visits.filter(baseOffer__id=buy.id)

    visits = visits.filter(visType=BuyRecommendVisit.VISITED)
    visits = dict([ (visit.recOffer.id, visit.time + timedelta(minutes=5),) for visit in visits.all() ])

    if user:
        connections = OfferConnection.objects.filter(user__id=user.id)
        connections = set([ conn.sale.id for conn in connections.all() if conn.sale ])
    else:
        connections = set()

    rankedSales = []
    curTime = datetime.now()
    for sale in sales:
        if limit and len(rankedSales) > limit:
            break
        rank = 0.0
        if not sale.visible() or sale.closed:
            continue

        if buy.fr != None:
            if sale.to.id == buy.fr.id:
                rank += 2.0
            else:
                continue

        if sale.ifrCity == buy.itoCity and sale.ifrCity:
            rank += 1.0

        if sale.itoCity == buy.ifrCity and sale.itoCity:
            rank += 1.0

        sale.connected = sale.id in connections

        sale.new = not sale.connected and \
                  sale.createTime > buy.createTime and \
                  visits.get(sale.id, curTime) >= curTime
        sale.visited = sale.id in visits
        sale.rank = rank
        rankedSales.append(sale)

    return sorted(rankedSales, key=lambda x: (not x.new, -x.rank, x.toTime))

def SaleFilterExtractParams(request, static=False, recommend=None):
    params = request.REQUEST
    owner = int(params.get("owner", 0))
    user = GetCurrentUser(request)

    recBuy = recommend
    if recBuy == None and params.get("recommend"):
        recBuy = int(params["recommend"])
    if type(recBuy) == int:
        recBuy = BuyOffer.objects.get(id=recBuy)

    if recBuy and (not user or recBuy.owner.id != user.id):
        raise RedirectExc("/offer/buy/{}".format(recBuy.id))

    if not recBuy:
        sales = _SaleExtractList(params)
    else:
        sales = SaleExtractRecommend(recBuy, user)

    count = max(0, int(params.get("count", 15)))
    totalpages = (len(sales) + count - 1) // count
    page = max(1, min(int(params.get("page", 1)), totalpages)) - 1
    block = sales[page*count:(page+1)*count]
    if recBuy:
        curTime = datetime.now()
        for sale in block:
            if not sale.visited:
                vis = BuyRecommendVisit(user=user,
                                        visType=BuyRecommendVisit.VISITED,
                                        time=curTime,
                                        baseOffer=recBuy,
                                        recOffer=sale)
                vis.save()

    return {
        "sales": sales,
        "saleblock": block,
        "page": page,
        "totalpages": totalpages,
        "profile": int(params.get("profile", 0)),
        "pagesid": "trips" if not static else "#",
        "static": static,
    }

def SaleIsConnected(request, id):
    if GetCurrentUser(request):
        return len(OfferConnection.objects.filter(user__id=GetCurrentUser(request).id,
                                                       sale__id=id).all()) > 0
    else:
        return False

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

def _BuyExtractList(params):
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
    return buys

def BuyExtractRecommend(sale, user=None, limit=None):
    buys = BuyOffer.objects.filter(to__id=sale.fr.id)
    buys = buys.exclude(owner__id=sale.owner.id)
    buys = buys.all()

    visits = SaleRecommendVisit.objects
    if user:
        visits = visits.filter(user__id=user.id)
    else:
        visits = visits.filter(baseOffer__id=sale.id)

    visits = visits.filter(visType=SaleRecommendVisit.VISITED)
    visits = dict([ (visit.recOffer.id, visit.time + timedelta(minutes=5),) for visit in visits.all() ])

    if user:
        connections = OfferConnection.objects.filter(user__id=user.id)
        connections = set([ conn.buy.id for conn in connections.all() if conn.buy ])
    else:
        connections = set()

    rankedBuy = []
    curTime = datetime.now()
    for buy in buys:
        if limit and len(rankedBuy) > limit:
            break
        rank = 0.0
        if not buy.visible() or buy.closed:
            continue

        if buy.fr != None:
            if buy.fr.id == sale.to.id:
                rank += 2.0
            else:
                continue

        if buy.ifrCity == sale.itoCity and buy.ifrCity:
            rank += 1.0

        if buy.itoCity == sale.ifrCity and buy.itoCity:
            rank += 1.0

        buy.connected = buy.id in connections

        buy.new = not buy.connected and \
                  buy.createTime > sale.createTime and \
                  visits.get(buy.id, curTime) >= curTime
        buy.visited = buy.id in visits
        buy.rank = rank
        rankedBuy.append(buy)
    return sorted(rankedBuy, key=lambda x: (not x.new, -x.rank, -x.id))

def BuyFilterExtractParams(request, static=False, recommend=None):
    params = request.REQUEST
    user = GetCurrentUser(request)

    recSale = recommend
    if recSale == None and params.get("recommend"):
        recSale = int(params["recommend"])
    if type(recSale) == int:
        recSale = SaleOffer.objects.get(id=recSale)

    if recSale and (not user or recSale.owner.id != user.id):
        raise RedirectExc("/offer/sale/{}".format(recSale.id))

    if not recSale:
        buys = _BuyExtractList(params)
    else:
        buys = BuyExtractRecommend(recSale, user)
    count = max(0, int(params.get("count", 15)))
    totalpages = (len(buys) + count - 1) // count
    page = max(1, min(int(params.get("page", 1)), totalpages)) - 1
    block = buys[page*count:(page+1)*count]
    if recSale:
        curTime = datetime.now()
        for buy in block:
            if not buy.visited:
                vis = SaleRecommendVisit(user=user,
                                         visType=SaleRecommendVisit.VISITED,
                                         time=curTime,
                                         baseOffer=recSale,
                                         recOffer=buy)
                vis.save()

    return {
        "buys": buys,
        "buyblock": block,
        "page": page,
        "static": static,
        "totalpages": totalpages,
        "profile": int(params.get("profile", 0)),
        "pagesid": "buys" if not static else "#",
    }

def BuyIsConnected(request, id):
    if GetCurrentUser(request):
        return len(OfferConnection.objects.filter(user__id=GetCurrentUser(request).id,
                                                  buy__id=id).all()) > 0
    else:
        return False
