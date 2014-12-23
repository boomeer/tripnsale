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
    conf2 = Conference(
        plusGuarant=conf,
        askGuarant=False,
        withGuarant=True,
    )
    conf2.save()
    conf2.users.add(*(list(conf.users.all()) + [guarant]))
    conf.plusGuarant = conf2
    conf.save()
    msg = SystemMsg(
        conf=conf2,
        content="Гарант подключен к конференции",
        time=datetime.now(),
    )
    msg.save()
    msg2 = SystemMsg(
        conf=conf,
        content="Гарант принял вашу заявку. Перейдите в отдельную конференцию по кнопке внизу диалога",
        time=datetime.now(),
    )
    msg2.save()
    return redirect("/user/im?conf={}".format(conf.id))
