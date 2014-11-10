from django.shortcuts import (
    redirect,
)
from django.template import RequestContext
from offer.models import (
    BuyOffer,
    SaleOffer,
)
from util.utils import (
    SafeView,
    RenderToResponse,
    CheckPost,
)
from user.utils import (
    GetCurrentUser,
    CheckAuth,
)
from datetime import datetime


@SafeView
def SaleListView(request):
    sales = SaleOffer.objects.all()
    return RenderToResponse("offer/sale/list.html", request, {
        "sales": sales,
    })


@SafeView
def BuyOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        CheckPost(request)
        CheckAuth(request)
        buy = BuyOffer(
            title=params.get("title", ""),
            costFrom=params.get("costFrom", None),
            costTo=params.get("costTo", None),
            guarant=params.get("guarant", False),
            owner=GetCurrentUser(request),
        )
        buy.save()
        return redirect("/")
    return RenderToResponse("offer/buy/add.html", request, {
    })


@SafeView
def SaleOfferAddView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        CheckPost(request)
        CheckAuth(request)
        sale = SaleOffer(
            fr=params.get("from", ""),
            frTime=datetime.strptime(params.get("fromTime", ""), "%d.%m.%Y"),
            to=params.get("to", ""),
            toTime=datetime.strptime(params.get("toTime", ""), "%d.%m.%Y"),
            deposit=params.get("deposit", None),
            guarant=params.get("guarant", False),
            owner=GetCurrentUser(request),
        )
        sale.save()
        return redirect("/")
    return RenderToResponse("offer/sale/add.html", request, {
    })


@SafeView
def SaleFilterView(request):
    params = request.REQUEST
    sales = SaleOffer.objects.filter(
        fr__startswith=params.get("from", ""),
        to__startswith=params.get("to", ""),
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
