from django.shortcuts import (
    redirect,
)
from django.template import RequestContext
from offer.models import (
    BuyOffer,
    SaleOffer,
)
from place.models import (
    Country,
)
from util.utils import (
    SafeView,
    RenderToResponse,
    CheckPost,
    StoreImage,
    AvatarBigSizeErr,
)
from user.utils import (
    GetCurrentUser,
    CheckAuth,
)
from gallery.utils import (
    CreateGallery,
    CreateGalleryPhoto,
)
from datetime import datetime


@SafeView
def SaleListView(request):
    return RenderToResponse("offer/sale/list.html", request, {
        "url": "/offer/sale/list",
    })


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
    sales = SaleOffer.objects.filter(
        fr__ititle__istartswith=params.get("from", ""),
        to__ititle__istartswith=params.get("to", ""),
    ).all()
    page = params.get("page", 1)
    count = params.get("count", 5)
    block = sales[(page-1)*count:page*count]
    return RenderToResponse("offer/sale/filter.html", request, {
        "sales": sales,
        "block": block,
    })


@SafeView
def SaleView(request, id):
    sale = SaleOffer.objects.get(id=id)
    return RenderToResponse("offer/sale/view.html", request, {
        "sale": sale,
    })


@SafeView
def BuyOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        CheckPost(request)
        CheckAuth(request)
        gallery = CreateGallery()
        buy = BuyOffer(
            title=params.get("title", ""),
            content=params.get("content", ""),
            costFrom=params.get("costFrom", None),
            costTo=params.get("costTo", None),
            guarant=params.get("guarant", False),
            gallery=gallery,
            owner=GetCurrentUser(request),
        )
        buy.save()
        return redirect("/offer/buy/list")
    return RenderToResponse("offer/buy/add.html", request, {
        "url": "/offer/buy",
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
        buy.costFrom = float(params.get("costFrom", 0).replace(",", "."))
        buy.costTo = float(params.get("costTo", 0).replace(",", "."))
        if not buy.gallery:
            buy.gallery = CreateGallery()
        for photo in request.FILES.getlist("photos"):
            ph = CreateGalleryPhoto(buy.gallery)
            try:
                StoreImage(photo, ph.img)
            except AvatarBigSizeErr:
                ph.delete()
        buy.save()
        return redirect("/offer/buy/edit/{}?msg=buy_edit_ok".format(buy.id))
    return RenderToResponse("offer/buy/edit.html", request, {
        "url": "/offer/buy/edit/{}/".format(buy.id),
        "buy": buy,
    })
        


@SafeView
def BuyListView(request):
    return RenderToResponse("offer/buy/list.html", request, {
        "url": "/offer/buy/list",
    })


@SafeView
def BuyFilterView(request):
    params = request.REQUEST
    buys = BuyOffer.objects.filter(
        title__istartswith=params.get("title", ""),
    ).all()
    page = params.get("page", 1)
    count = params.get("count", 5)
    block = buys[(page-1)*count:page*count]
    return RenderToResponse("offer/buy/filter.html", request, {
        "buys": buys,
        "block": block,
    })


@SafeView
def BuyView(request, id):
    buy = BuyOffer.objects.get(id=id)
    return RenderToResponse("offer/buy/view.html", request, {
        "buy": buy,
    })


