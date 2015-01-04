from django.shortcuts import render
from util.utils import RenderToResponse
from infos.models import (
    Backmsg,
)
from valute.models import (
    Valute,
)
from util.utils import (
    SafeView,
    TsExc,
    RedirectExc,
    RenderToResponse,
)
from util.msg import (
    GetBackmsgMsg,
)
from user.utils import (
    GetCurrentUser,
)

class BackmsgErr(TsExc):
    def __init__(self, msg):
        super().__init__(msg)
        self.status = msg

class EmptyMessageErr(BackmsgErr):
    def __init__(self):
        super().__init__("message_is_empty")

class EmptyAnswerEmailErr(BackmsgErr):
    def __init__(self):
        super().__init__("empty_answer_email")

@SafeView
def InfoView(request, name):
    params = request.REQUEST
    user = GetCurrentUser(request)
    if name == "contact-form":
        if params.get("act", "") == "sendMsg":
            try:
                if not params.get("body", "").strip():
                    raise EmptyMessageErr

                if user:
                    email = params.get("email", user.email)
                    msg = Backmsg(body=params["body"],
                                  email=email,
                                  user=user,
                                  name=params.get("name", ""))
                else:
                    if not params.get("email", ""):
                        raise EmptyAnswerEmailErr
                    email = params["email"]
                    msg = Backmsg(body=params["body"],
                                  email=email,
                                  user=None,
                                  name=params.get("name", ""))
                msg.save()
                return RenderToResponse("infos/contact-sent.html", request, {
                    "email": email
                })
            except TsExc as e:
                raise RedirectExc("/info/contact-form/?err={}".format(e.status))
        else:
            return RenderToResponse("infos/with_base.html", request, {
                "err": GetBackmsgMsg(params.get("err", "")),
                "filepath": "infos/contact-form.html",
                "email": user.email if user else "",
                "name": "{} {}".format(user.first_name, user.last_name) if user else ""
            })
    elif name == "compare":
        usdcourse = Valute.objects.filter(fromId__exact="USD")[0]
        return RenderToResponse("infos/compare.html", request, {
            "usd": usdcourse,
        })
    else:
        return RenderToResponse("infos/with_base.html", request, {
            "filepath": "infos/{}.html".format(name),
        })

