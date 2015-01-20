from django.shortcuts import (
    redirect,
)
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template import RequestContext
from offer.models import (
    BuyOffer,
    SaleOffer,
    OfferConnection,
)
from offer.utils import (
    SaleEditErr,
    ExtractSaleFields,
    SaleFilterExtractParams,
    SaleExtractRecommend,
    SaleIsConnected,
    BuyEditErr,
    ExtractBuyFields,
    BuyExtractRecommend,
    BuyFilterExtractParams,
    BuyIsConnected,
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
    ParseBool,
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

@SafeView
def SaleListView(request):
    filterparams = SaleFilterExtractParams(request, static=True)
    filterparams.update({ "url": "/offer/sale/list" })
    return RenderToResponse("offer/sale/list.html", request, filterparams)

@SafeView
def SaleOfferView(request, id):
    sale = SaleOffer.objects.get(exact__id=int(id))
    return RenderToResponse("offer/sale/view.html", request, { "sale": sale })


@login_required(login_url="/user/auth/")
@SafeView
def SaleOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    owner = GetCurrentUser(request)
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
                owner=owner,
                createTime=datetime.now(),
            )
            sale.save()
            # backref = params.get("backref", "/offer/sale/list#trip{}".format(sale.id))
            if BuyExtractRecommend(sale, owner, limit=1):
                backref = "/offer/sale/recommend/{}?first_time=true".format(sale.id)
            else:
                backref = "/offer/sale/list#trip{}".format(sale.id)
            return redirect(backref)
        except SaleEditErr as e:
            raise RedirectExc("/offer/sale/add/?err={}".format(e.status))
    else:
        return RenderToResponse("offer/sale/add.html", request, {
            "url": "/offer/sale/add/",
            "countries": GetCountries(),
            "err": GetSaleAddMsg(params.get("err", ""))
        })

@SafeView
def SaleEditView(request, id):
    params = request.REQUEST
    sale = SaleOffer.objects.get(id=id)
    act = params.get("act", "")
    if sale.owner != GetCurrentUser(request):
        return redirect("/offer/sale/{}".format(id))
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
            backref = params.get("backref", "/offer/sale/list/#trip{}".format(sale.id))
            return redirect(backref)
        except SaleEditErr as e:
            raise RedirectExc("/offer/sale/edit/{}?err={}".format(sale.id, e.status))
    else:
        return RenderToResponse("offer/sale/edit.html", request, {
            "sale": sale,
            "countries": GetCountries(),
            "err": GetSaleAddMsg(params.get("err", "")),
        })

@SafeView
def SaleFilterView(request):
    return RenderToResponse("offer/sale/filter.html", request,
                            SaleFilterExtractParams(request))


@SafeView
def SaleRemoveView(request):
    params = request.REQUEST
    sale = SaleOffer.objects.get(id=params.get("id", 0))
    if sale.owner == GetCurrentUser(request):
        sale.removed = True
        sale.save()
    if params.get("async", False):
        return JsonResponse({"result": "ok"})
    else:
        backref = params.get("backref", "/offer/sale/list/")
        return redirect(backref)

@SafeView
def SaleCloseView(request):
    params = request.REQUEST

    sale = SaleOffer.objects.get(id=params.get("id", 0))
    if sale.owner == GetCurrentUser(request):
        revert = ParseBool(params.get("revert", ""))
        sale.closed = not revert
        sale.save()

    if params.get("async", False):
        return JsonResponse({"result": "ok"})
    else:
        backref = params.get("backref", "/offer/sale/list/#trip{}".format(sale.id))
        return redirect(backref)


@SafeView
def SaleView(request, id):
    sale = SaleOffer.objects.get(id=id)
    if not sale.visible():
        raise Exception("not found")
    return RenderToResponse("offer/sale/view.html", request, {
        "sale": sale,
        "connected": SaleIsConnected(request, id),
    })

@SafeView
def SalePreview(request, id):
    params = request.REQUEST
    sale = SaleOffer.objects.get(id=id)
    if not sale.visible():
        raise Exception("not found")

    return RenderToResponse("offer/sale/preview.html", request, {
        "sale": sale,
        "editBackref": params.get("editBackref", ""),
        "connected": SaleIsConnected(request, id),
    })

@SafeView
def SaleRecommendView(request, id):
    params = request.REQUEST
    sale = SaleOffer.objects.get(id=id)
    if sale.owner != GetCurrentUser(request):
        return redirect("/offer/sale/{}".format(id))

    filterparams = BuyFilterExtractParams(request, static=True, recommend=sale)
    filterparams["recSale"] = sale
    filterparams["firstTime"] = ParseBool(params.get("first_time", ""))
    return RenderToResponse("offer/sale/recommend.html", request, filterparams)



@login_required(login_url="/user/auth/")
@SafeView
def BuyOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    owner = GetCurrentUser(request)
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
                owner=owner,
                createTime=datetime.now(),
            )
            buy.save()
            VerifyPhotos(params.get("token", ""))
            # backref = params.get("backref", "/offer/buy/list#buy{}".format(buy.id))
            if SaleExtractRecommend(buy, owner, limit=1):
                backref = "/offer/buy/recommend/{}?first_time=true".format(buy.id)
            else:
                backref = "/offer/buy/list#buy{}".format(buy.id)
            return redirect(backref)
        except BuyEditErr as e:
            raise RedirectExc("/offer/buy/add?err={}".format(e.status))
    else:
        gallery = CreateGallery()
        token = GetNewId()
        return RenderToResponse("offer/buy/add.html", request, {
            "url": "/offer/buy/add/",
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

            backref = params.get("backref", "/offer/buy/list/#buy{}".format(buy.id))
            return redirect(backref)
        except BuyEditErr as e:
            raise RedirectExc("/offer/buy/edit/{}?err={}".format(buy.id, e.status))
    elif act == "makeHead":
        pic = Photo.objects.get(id=params.get("picId"))
        pic.gallery.head = pic
        pic.gallery.save()
        backref = params.get("backref", "/offer/buy/edit/{}".format(buy.id))
        return redirect(backref)
    elif act == "erasePic":
        pic = Photo.objects.get(id=params.get("picId"))
        buy.gallery.er(pic)
        backref = params.get("backref", "/offer/buy/edit/{}".format(buy.id))
        return redirect(backref)
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
    if params.get("async", False):
        return JsonResponse({"result": "ok"})
    else:
        backref = params.get("backref", "/offer/buy/list/")
        return redirect(backref)


@SafeView
def BuyCloseView(request):
    params = request.REQUEST
    buy = BuyOffer.objects.get(id=params.get("id", 0))
    if buy.owner == GetCurrentUser(request):
        revert = ParseBool(params.get("revert", ""))
        buy.closed = not revert
        buy.save()

    if params.get("async", False):
        return JsonResponse({"result": "ok"})
    else:
        backref = params.get("backref", "/offer/buy/list#buy{}".format(buy.id))
        return redirect(backref)

@SafeView
def BuyListView(request):
    namespace = BuyFilterExtractParams(request, True)
    namespace["url"] = "/offer/buy/list"
    return RenderToResponse("offer/buy/list.html", request, namespace)

@SafeView
def BuyFilterView(request):
    return RenderToResponse("offer/buy/filter.html", request,
        BuyFilterExtractParams(request))

@SafeView
def BuyView(request, id):
    buy = BuyOffer.objects.get(id=id)
    if not buy.visible():
        raise Exception("not found")
    return RenderToResponse("offer/buy/view.html", request, {
        "buy": buy,
        "connected": BuyIsConnected(request, id),
    })

@SafeView
def BuyPreview(request, id):
    params = request.REQUEST
    buy = BuyOffer.objects.get(id=id)
    if not buy.visible():
        raise Exception("not found")
    return RenderToResponse("offer/buy/preview.html", request, {
        "buy": buy,
        "editBackref": params.get("editBackref", ""),
        "connected": BuyIsConnected(request, id),
    })

@SafeView
def BuyRecommendView(request, id):
    params = request.REQUEST
    buy = BuyOffer.objects.get(id=id)
    if buy.owner != GetCurrentUser(request):
        return redirect("/offer/buy/{}".format(id))

    filterparams = SaleFilterExtractParams(request, static=True, recommend=buy)
    filterparams["recBuy"] = buy
    filterparams["firstTime"] = ParseBool(params.get("first_time", ""))
    return RenderToResponse("offer/buy/recommend.html", request, filterparams)
