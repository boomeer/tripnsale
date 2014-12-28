from django.shortcuts import (
    redirect,
)
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template import RequestContext
from offer.models import (
    BuyOffer,
    SaleOffer,
)
from place.models import (
    Country,
)
from place.utils import (
    GetCountries,
)
from util.utils import (
    ValidFilter,
    TsExc,
    RedirectExc,
)
from util.msg import (
    GetBuyEditMsg,
    GetSaleAddMsg,
)
from util.utils import (
    SafeView,
    RenderToResponse,
    CheckPost,
    GetNewId,
)
from user.utils import (
    GetCurrentUser,
    CheckAuth,
)
from gallery.utils import (
    CreateGallery,
    CreateGalleryPhoto,
    StoreImage,
    MakeThumbnail,
    VerifyPhotos,
)
from gallery.models import (
    Gallery,
    Photo,
)
from datetime import datetime

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

@SafeView
def SaleListView(request):
    return RenderToResponse("offer/sale/list.html", request, {
        "url": "/offer/sale/list",
    })

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

@login_required(login_url="/user/auth/")
@SafeView
def SaleOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        try:
            CheckPost(request)
            CheckAuth(request)

            fr, to, frTime, toTime, deposit = ExtractSaleFields(params)
            sale = SaleOffer(
                content=params.get("content", ""),
                fr=fr,
                frCity=params.get("frCity", ""),
                ifrCity=params.get("frCity", "").lower(),
                frTime=frTime,
                to=to,
                toCity=params.get("toCity", ""),
                itoCity=params.get("toCity", "").lower(),
                toTime=toTime,
                deposit=deposit,
                guarant=params.get("guarant", False),
                owner=GetCurrentUser(request),
                createTime=datetime.now(),
            )
            sale.save()
            return redirect("/offer/sale/list#trip{}".format(sale.id))
        except SaleEditErr as e:
            raise RedirectExc("/offer/sale/?err={}".format(e.status))
    return RenderToResponse("offer/sale/add.html", request, {
        "url": "/offer/sale",
        "countries": GetCountries(),
        "err": GetSaleAddMsg(params.get("err", ""))
    })

@SafeView
def SaleEditView(request, id):
    params = request.REQUEST
    sale = SaleOffer.objects.get(id=id)
    act = params.get("act", "")
    if sale.owner != GetCurrentUser(request):
        return redirect("/")
    if act == "edit":
        try:
            CheckPost(request)
            fr, to, frTime, toTime, deposit = ExtractSaleFields(params)

            sale.content = params.get("content", "")
            sale.fr = fr
            sale.frCity = params.get("frCity", "")
            sale.ifrCity = params.get("frCity", "").lower()
            sale.frTime = frTime;
            sale.to = to
            sale.toCity = params.get("toCity", "")
            sale.itoCity = params.get("toCity", "").lower()
            sale.toTime = toTime
            sale.deposit = deposit
            sale.guarant = params.get("guarant", False)
            sale.save()
            return redirect("/offer/sale/list/#{}".format(sale.id))
        except SaleEditErr as e:
            raise RedirectExc("/offer/sale/edit/{}?err={}".format(sale.id, e.status))
    return RenderToResponse("offer/sale/edit.html", request, {
        "sale": sale,
        "countries": GetCountries(),
        "err": GetSaleAddMsg(params.get("err", "")),
    })


@SafeView
def SaleFilterView(request):
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
    page = max(0, min(int(params.get("page", 1)), totalpages - 1))
    block = sales[page*count:(page+1)*count]
    return RenderToResponse("offer/sale/filter.html", request, {
        "sales": sales,
        "block": block,
        "page": page,
        "totalpages": totalpages,
        "profile": int(params.get("profile", 0)),
        "pagesid": "trips"
    })


@SafeView
def SaleRemoveView(request):
    params = request.REQUEST
    sale = SaleOffer.objects.get(id=params.get("id", 0))
    if sale.owner == GetCurrentUser(request):
        sale.removed = True
        sale.save()
    backref = params.get("backref", "/user/profile")
    return redirect(backref)


@SafeView
def SaleCloseView(request):
    params = request.REQUEST
    sale = SaleOffer.objects.get(id=params.get("id", 0))
    if sale.owner == GetCurrentUser(request):
        revert = bool(params.get("revert", False))
        sale.closed = not revert
        sale.save()
    backref = params.get("backref", "/user/profile")
    return redirect(backref)


@SafeView
def SaleView(request, id):
    sale = SaleOffer.objects.get(id=id)
    if not sale.visible():
        raise Exception("not found")
    return RenderToResponse("offer/sale/view.html", request, {
        "sale": sale,
    })

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

@login_required(login_url="/user/auth/")
@SafeView
def BuyOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        try:
            CheckPost(request)
            CheckAuth(request)

            fr, to, title, costFrom, costTo = ExtractBuyFields(params)

            gallery = Gallery.objects.get(token=params.get("gallery", ""))
            buy = BuyOffer(
                title=title,
                ititle=title.lower(),
                content=params.get("content", ""),
                costFrom=costFrom,
                costTo=costTo,
                guarant=params.get("guarant", False),
                fr=fr,
                frCity=params.get("frCity", ""),
                ifrCity=params.get("frCity", "").lower(),
                to=to,
                toCity=params.get("toCity", ""),
                itoCity=params.get("toCity", "").lower(),
                gallery=gallery,
                owner=GetCurrentUser(request),
                createTime=datetime.now(),
            )
            buy.save()
            VerifyPhotos(params.get("token", ""))
            return redirect("/offer/buy/list#buy{}".format(buy.id))
        except BuyEditErr as e:
            raise RedirectExc("/offer/buy/?err={}".format(e.status))
    gallery = CreateGallery()
    token = GetNewId()
    return RenderToResponse("offer/buy/add.html", request, {
        "url": "/offer/buy",
        "gallery": gallery,
        "token": token,
        "countries": GetCountries(),
        "err": GetBuyEditMsg(params.get("err", ""))
    })


@SafeView
def BuyEditView(request, id):
    params = request.REQUEST
    act = params.get("act", "")
    buy = BuyOffer.objects.get(id=id)
    user = GetCurrentUser(request)
    if buy.owner != user:
        return redirect("/")
    if act == "edit":
        try:
            CheckPost(request)
            fr, to, title, costFrom, costTo = ExtractBuyFields(params)
            buy.title = title
            buy.content = params.get("content", "")
            buy.costFrom = costFrom
            buy.costTo = costTo
            buy.fr = fr
            buy.frCity = params.get("frCity", "")
            buy.ifrCity = params.get("frCity", "").lower()
            buy.to = to
            buy.toCity = params.get("toCity", "")
            buy.itoCity = params.get("toCity", "").lower()
            buy.guarant = params.get("guarant", False)
            buy.save()
            VerifyPhotos(params.get("token", ""))
            return redirect("/offer/buy/list/#{}".format(buy.id))
        except BuyEditErr as e:
            raise RedirectExc("/offer/buy/edit/{}?err={}".format(buy.id, e.status))
    elif act == "makeHead":
        pic = Photo.objects.get(id=params.get("picId"))
        pic.gallery.head = pic
        pic.gallery.save()
        return redirect("/offer/buy/edit/{}".format(buy.id))
    elif act == "erasePic":
        pic = Photo.objects.get(id=params.get("picId"))
        buy.gallery.er(pic)
        return redirect("/offer/buy/edit/{}".format(buy.id))
    return RenderToResponse("offer/buy/edit.html", request, {
        "url": "/offer/buy/edit/{}/".format(buy.id),
        "buy": buy,
        "err": GetBuyEditMsg(params.get("err", "")),
        "token": GetNewId(),
        "countries": GetCountries(),
    })


@SafeView
def BuyRemoveView(request):
    params = request.REQUEST
    buy = BuyOffer.objects.get(id=params.get("id", 0))
    if buy.owner == GetCurrentUser(request):
        buy.removed = True
        buy.save()
    backref = params.get("backref", "/user/profile")
    return redirect(backref)


@SafeView
def BuyCloseView(request):
    params = request.REQUEST
    buy = BuyOffer.objects.get(id=params.get("id", 0))
    if buy.owner == GetCurrentUser(request):
        revert = bool(params.get("revert", False))
        buy.closed = not revert
        buy.save()
    backref = params.get("backref", "/user/profile")
    return redirect(backref)


@SafeView
def BuyListView(request):
    return RenderToResponse("offer/buy/list.html", request, {
        "url": "/offer/buy/list",
    })


@SafeView
def BuyFilterView(request):
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
    page = max(0, min(int(params.get("page", 1)), totalpages - 1))
    block = buys[page*count:(page+1)*count]
    return RenderToResponse("offer/buy/filter.html", request, {
        "buys": buys,
        "block": block,
        "page": page,
        "totalpages": totalpages,
        "profile": int(params.get("profile", 0)),
        "pagesid": "buys"
    })


@SafeView
def BuyView(request, id):
    buy = BuyOffer.objects.get(id=id)
    if not buy.visible():
        raise Exception("not found")
    return RenderToResponse("offer/buy/view.html", request, {
        "buy": buy,
    })


