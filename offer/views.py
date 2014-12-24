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
        super().__init__("fromdate_field_is_empty")

class SaleFrDateInvalidErr (SaleEditErr):
    def __init__(self):
        super().__init__("fromdate_field_is_invalid")

class SaleFrCountryMissingErr (SaleEditErr):
    def __init__(self):
        super().__init__("fromcountry_field_is_empty")

class SaleFrCountryInvalidErr (SaleEditErr):
    def __init__(self):
        super().__init__("fromcountry_field_is_invalid")

class SaleToDateMissingErr (SaleEditErr):
    def __init__(self):
        super().__init__("todate_field_is_empty")

class SaleToDateInvalidErr (SaleEditErr):
    def __init__(self):
        super().__init__("todate_field_is_invalid")

class SaleToCountryMissingErr (SaleEditErr):
    def __init__(self):
        super().__init__("tocountry_field_is_empty")

class SaleToCountryInvalidErr (SaleEditErr):
    def __init__(self):
        super().__init__("tocountry_field_is_invalid")

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

    try:
        deposit = round(float(params.get("deposit", "0").replace(",", ".").strip()))
    except ValueError:
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
            return redirect("/offer/sale/list")
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
    '''
    sales = sales.filter(
        fr__ititle__istartswith=params.get("from", "").lower(),
        to__ititle__istartswith=params.get("to", "").lower(),
    )
    '''
    if owner:
        sales = sales.filter(owner__id=owner)
    sales = sales.all()
    sales = [sale for sale in sales if ValidFilter(sale.fr.title + " " + sale.frCity,
                                                    params.get("from", "")) \
                and ValidFilter(sale.to.title + " " + sale.toCity, params.get("to", ""))]
    sales = sorted(sales, key=lambda sale: (sale.closed, -sale.isCurrent(), sale.toEnd(),))
    page = params.get("page", 1)
    count = params.get("count", 5)
    block = sales[(page-1)*count:page*count]
    return RenderToResponse("offer/sale/filter.html", request, {
        "sales": sales,
        "block": block,
        "profile": int(params.get("profile", 0)),
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

@login_required(login_url="/user/auth/")
@SafeView
def BuyOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        CheckPost(request)
        CheckAuth(request)
        gallery = Gallery.objects.get(token=params.get("gallery", ""))
        fr = Country.objects.get(name=params.get("from", ""))
        to = Country.objects.get(name=params.get("to", ""))
        buy = BuyOffer(
            title=params.get("title", ""),
            ititle=params.get("title", "").lower(),
            content=params.get("content", ""),
            costFrom=params.get("costFrom", None),
            costTo=params.get("costTo", None),
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
        return redirect("/offer/buy/list")
    gallery = CreateGallery()
    token = GetNewId()
    return RenderToResponse("offer/buy/add.html", request, {
        "url": "/offer/buy",
        "gallery": gallery,
        "token": token,
        "countries": GetCountries(),
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
        CheckPost(request)
        fr = Country.objects.get(name=params.get("from", ""))
        to = Country.objects.get(name=params.get("to", ""))
        buy.title = params.get("title", "")
        buy.content = params.get("content", "")
        buy.costFrom = float(params.get("costFrom", "0").replace(",", "."))
        buy.costTo = float(params.get("costTo", "0").replace(",", "."))
        buy.fr = fr
        buy.frCity = params.get("frCity", "")
        buy.ifrCity = params.get("frCity", "").lower()
        buy.to = to
        buy.toCity = params.get("toCity", "")
        buy.itoCity = params.get("toCity", "").lower()
        buy.guarant = params.get("guarant", False)
        buy.save()
        VerifyPhotos(params.get("token", ""))
        return redirect("/offer/buy/edit/{}?msg=buy_edit_ok".format(buy.id))
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
        "succMsg": GetBuyEditMsg(params.get("msg", "")),
        "failMsg": GetBuyEditMsg(params.get("err", "")),
        "token": GetNewId(),
        "countries": GetCountries(),
    })


@SafeView
def BuyRemoveView(request):
    params = request.REQUEST
    buy = BuyOffer.objects.get(id=params.get("id", 0))
    if buy.owner == GetCurrentUser(request):
        revert = bool(params.get("revert", False))
        buy.closed = not revert
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
    '''
    buys = buys.filter(
        ititle__istartswith=params.get("title", "").lower(),
    )
    '''
    if owner:
        buys = buys.filter(owner__id=owner)
    buys = buys.all()
    buys = [buy for buy in buys if ValidFilter(buy.title + " " + buy.content,
                params.get("title", ""))]
    buys = sorted(buys, key=lambda buy: (buy.closed, -buy.id,))
    page = params.get("page", 1)
    count = params.get("count", 5)
    block = buys[(page-1)*count:page*count]
    return RenderToResponse("offer/buy/filter.html", request, {
        "buys": buys,
        "block": block,
        "profile": int(params.get("profile", 0)),
    })


@SafeView
def BuyView(request, id):
    buy = BuyOffer.objects.get(id=id)
    if not buy.visible():
        raise Exception("not found")
    return RenderToResponse("offer/buy/view.html", request, {
        "buy": buy,
    })


