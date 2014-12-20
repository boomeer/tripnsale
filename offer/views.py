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
from util.msg import (
    GetBuyEditMsg,
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
from util.utils import ValidFilter
from datetime import datetime


@SafeView
def SaleListView(request):
    return RenderToResponse("offer/sale/list.html", request, {
        "url": "/offer/sale/list",
    })

@login_required(login_url="/user/auth/")
@SafeView
def SaleOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        CheckPost(request)
        CheckAuth(request)
        fr = Country.objects.get(name=params.get("from", ""))
        to = Country.objects.get(name=params.get("to", ""))
        sale = SaleOffer(
            fr=fr,
            frCity=params.get("frCity", ""),
            ifrCity=params.get("frCity", "").lower(),
            frTime=datetime.strptime(params.get("fromTime", ""), "%d.%m.%Y"),
            to=to,
            toCity=params.get("toCity", ""),
            itoCity=params.get("toCity", "").lower(),
            toTime=datetime.strptime(params.get("toTime", ""), "%d.%m.%Y"),
            deposit=params.get("deposit", None),
            guarant=params.get("guarant", False),
            owner=GetCurrentUser(request),
            createTime=datetime.now(),
        )
        sale.save()
        return redirect("/offer/sale/list")
    countries = Country.objects.all()
    return RenderToResponse("offer/sale/add.html", request, {
        "url": "/offer/sale",
        "countries": countries,
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
    return redirect("/user/profile")


@SafeView
def SaleCloseView(request):
    params = request.REQUEST
    sale = SaleOffer.objects.get(id=params.get("id", 0))
    if sale.owner == GetCurrentUser(request):
        sale.closed = True
        sale.save()
    return redirect("/user/profile")


@SafeView
def SaleView(request, id):
    sale = SaleOffer.objects.get(id=id)
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
        buy = BuyOffer(
            title=params.get("title", ""),
            ititle=params.get("title", "").lower(),
            content=params.get("content", ""),
            costFrom=params.get("costFrom", None),
            costTo=params.get("costTo", None),
            guarant=params.get("guarant", False),
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
        buy.title = params.get("title", "")
        buy.content = params.get("content", "")
        buy.costFrom = float(params.get("costFrom", "0").replace(",", "."))
        buy.costTo = float(params.get("costTo", "0").replace(",", "."))
        VerifyPhotos(params.get("token", ""))
        return redirect("/offer/buy/edit/{}?msg=buy_edit_ok".format(buy.id))
    elif act == "makeHead":
        pic = Photo.objects.get(id=params.get("picId"))
        pic.gallery.head = pic
        pic.gallery.save()
    elif act == "erasePic":
        pic = Photo.objects.get(id=params.get("picId"))
        pic.delete()
    return RenderToResponse("offer/buy/edit.html", request, {
        "url": "/offer/buy/edit/{}/".format(buy.id),
        "buy": buy,
        "succMsg": GetBuyEditMsg(params.get("msg", "")),
        "failMsg": GetBuyEditMsg(params.get("err", "")),
        "token": GetNewId(),
    })


@SafeView
def BuyRemoveView(request):
    params = request.REQUEST
    buy = BuyOffer.objects.get(id=params.get("id", 0))
    if buy.owner == GetCurrentUser(request):
        buy.removed = True
        buy.save()
    return redirect("/user/profile")


@SafeView
def BuyCloseView(request):
    params = request.REQUEST
    buy = BuyOffer.objects.get(id=params.get("id", 0))
    if buy.owner == GetCurrentUser(request):
        buy.closed = True
        buy.save()
    return redirect("/user/profile")


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
    return RenderToResponse("offer/buy/view.html", request, {
        "buy": buy,
    })


