from django.shortcuts import redirect
from user.models import Conference, SystemMsg
from util.utils import (
    RenderToResponse,
    SafeView,
)
from datetime import datetime
from user.utils import GetCurrentUser


@SafeView
def AsksView(request):
    confs = Conference.objects.filter(askGuarant=True).all()
    return RenderToResponse("guarant/asks.html", request, {
        "confs": confs,
    })


@SafeView
def AcceptView(request, confId):
    conf = Conference.objects.get(id=confId)
    if not conf.askGuarant:
        raise Exception("askGuarant == False")
    guarant = GetCurrentUser(request)
    if not guarant.guarant:
        raise Exception("You aren't guarant")
    conf.askGuarant = False
    conf.withGuarant = True
    conf.save()
    conf.users.add(guarant)
    msg = SystemMsg(
        conf=conf,
        content="Гарант подключен к конференции",
        time=datetime.now(),
    )
    msg.save()
    return redirect("/user/im?conf={}".format(conf.id))
