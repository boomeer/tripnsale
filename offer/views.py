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
def MainView(request):
    buys = BuyOffer.objects.all()
    sales = SaleOffer.objects.all()
    return RenderToResponse("offer/main.html", request, {
        "buys": buys,
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
            owner=GetCurrentUser(request),
        )
        sale.save()
        return redirect("/")
    return RenderToResponse("offer/sale/add.html", request, {
    })
