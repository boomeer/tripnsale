from django.shortcuts import (
    render,
    HttpResponse,
    render_to_response,
    redirect,
)
from django.template import RequestContext
from offer.models import (
    BuyOffer,
    SaleOffer,
)
from util.utils import (
    SafeView,
)
from datetime import datetime


@SafeView
def MainView(request):
    buys = BuyOffer.objects.all()
    sales = SaleOffer.objects.all()
    return render_to_response("offer/main.html", RequestContext(request, {
        "buys": buys,
        "sales": sales,
    }))


@SafeView
def BuyOfferAdd(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        buy = BuyOffer(
            title=params.get("title", ""),
            costFrom=params.get("costFrom", None),
            costTo=params.get("costTo", None),
        )
        buy.save()
        return redirect("/")
    return render_to_response("offer/buy/add.html", RequestContext(request, {
    }))


@SafeView
def SaleOfferAdd(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "add":
        sale = SaleOffer(
            fr=params.get("from", ""),
            frTime=datetime.strptime(params.get("fromTime", ""), "%d.%m.%Y"),
            to=params.get("to", ""),
            toTime=datetime.strptime(params.get("toTime", ""), "%d.%m.%Y"),
            deposit=params.get("deposit", None),
        )
        sale.save()
        return redirect("/")
    return render_to_response("offer/sale/add.html", RequestContext(request, {
    }))
