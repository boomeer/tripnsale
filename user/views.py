from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
import tripnsale.settings as settings
from util.utils import (
    SafeView,
    TsExc,
    RedirectExc,
    RenderToResponse,
    CheckPost,
    GetNewId,
)
from util.msg import(
    GetEditProfileMsg,
    GetRegMsg,
    GetUserRecoverMsg,
)
from gallery.utils import StoreImage, MakeThumbnail
from user.models import *
from user.utils import *
from place.models import (
    Country,
)
from place.utils import (
    GetCountries,
)
from user.utils import (
    GetCurrentUser,
    GetDjUserByUser,
)
from offer.utils import (
    CheckConnection,
    SendOfferMail,
)
from offer.models import (
    BuyOffer,
    SaleOffer,
    OfferConnection,
)
import re
from datetime import datetime


class EditErr(TsExc):
    def __init__(self, msg):
        super().__init__(msg)
        self.status = msg

class RegErr(TsExc):
    def __init__(self, msg):
        super().__init__(msg)
        self.status = msg

class UsernameIsInvalidErr(RegErr):
    def __init__(self):
        super().__init__("username_is_invalid")

class EmailIsInvalidErr(RegErr):
    def __init__(self):
        super().__init__("email_is_invalid")

class ShortUsernameErr(RegErr):
    def __init__(self):
        super().__init__("username_is_too_short")

class LongUsernameErr(RegErr):
    def __init__(self):
        super().__init__("username_is_too_long")

class DuplicateUsernameErr(RegErr):
    def __init__(self):
        super().__init__("username_is_not_unique")

class DuplicateEmailErr(RegErr):
    def __init__(self):
        super().__init__("email_is_not_unique")

class PasswordIsInvalidErr(RegErr, EditErr):
    def __init__(self):
        super().__init__("password_is_invalid")

class BadPasswordLengthErr(RegErr, EditErr):
    def __init__(self):
        super().__init__("bad_password_len")

class PasswordsAreNotEqualErr(RegErr, EditErr):
    def __init__(self):
        super().__init__("passwords_are_not_equal")

class OfferNotAgreedErr(RegErr):
    def __init__(self):
        super().__init__("offer_wasnt_be_agreed")

class RequiredFieldsMissingErr(RegErr):
    def __init__(self):
        super().__init__("required_fields_missed")

class MsgCannotBeEmpty(TsExc):
    def __init__(self):
        super().__init__("msg_cannot_be_empty")

@SafeView
def AuthView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "login":
        CheckPost(request)
        djUser = authenticate(
            username=params.get("email", "").lower(),
            password=params.get("password", ""),
        )
        user = GetUserByDjUser(djUser)
        if user:
            if not user.activated:
                raise RedirectExc("/user/auth?msgLogin=user_is_not_activated")
            user.remoteAddr = request.META["REMOTE_ADDR"]
            user.save()
            login(request, djUser)
        else:
            raise RedirectExc("/user/auth/?msgLogin=wrong_login_or_password")
        backref = params.get("next", "/")
        if not backref:
            backref = "/"
        return redirect(backref)
    elif act == "reg":
        try:
            CheckPost(request)
            if not params.get("firstName", "").strip() or not params.get("lastName", "").strip():
                raise RequiredFieldsMissingErr

            if params["password"] != params["password2"]:
                raise PasswordsAreNotEqualErr
            if not re.compile("^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+$").match(params["email"]):
                raise EmailIsInvalidErr
            if not (3 <= len(params["password"]) <= 20):
                raise BadPasswordLengthErr
            if not params.get("offert", 0):
                raise OfferNotAgreedErr
            country = Country.objects.get(name=params.get("country", 0))

            if User.objects.filter(username=params["email"]).count():
                raise DuplicateEmailErr

            user = User.objects.create_user(
                params.get("email", "").lower(),
                params.get("email", "").lower(),
                params.get("password", ""),
                first_name=params.get("firstName", ""),
                last_name=params.get("lastName", ""),
                country=country,
                city=params.get("city", ""),
                remoteAddr=request.META["REMOTE_ADDR"],
                regRemoteAddr=request.META["REMOTE_ADDR"],
                activateCode=GetNewId(),
                activated=not settings.ENABLE_ACTIVATION,
            )
            user.save()

            if settings.ENABLE_ACTIVATION:
                SendActivateMail(user)
                return RenderToResponse("user/auth_success.html", request, {
                            "email": params.get("email", ""),
                        })
            else:
                user = authenticate(
                    username=user.username,
                    password=params.get("password", ""),
                )
                login(request, user)
                backref = params.get("next", "/user/profile/?firsttime=1")
                return redirect(backref)
        except RegErr as e:
            raise RedirectExc("/user/auth/?msgReg={}".format(e.status))
    return RenderToResponse("user/auth.html", request, {
        "countries": GetCountries(),
        "msgLogin": GetRegMsg(params.get("msgLogin", "")),
        "msgReg": GetRegMsg(params.get("msgReg", "")),
        "next": params.get("next", ""),
    })


@SafeView
def ActivateView(request, code):
    user = User.objects.get(activateCode=code)
    user.activated = True
    user.save()
    djUser = GetDjUserByUser(user)
    djUser.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, djUser)
    return redirect("/user/profile/?firsttime=1")


@SafeView
def LogoutView(request):
    logout(request)
    backref = request.REQUEST.get("backref", "/")
    if not backref:
        backref = "/"
    return redirect(backref)


@login_required(login_url="/user/auth/")
@SafeView
def ImView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "send":
        user = GetCurrentUser(request)
        content = params.get("content", "").strip()
        if not content:
            raise MsgCannotbeEmptyErr
        conf = Conference.objects.get(id=params.get("conf", 0))
        msg = ConferenceMsg(
            conf=conf,
            fr=user,
            content=content,
            time=datetime.now(),
        )
        msg.save()
        return RenderJson({"result": "ok"})
    elif act == "askGuarant":
        conf = Conference.objects.get(id=params.get("conf"))
        if conf.askGuarant or conf.plusGuarant:
            raise Exception("bad request")
        conf.askGuarant = True
        conf.save()
        msg = SystemMsg(
            conf=conf,
            content="Запрос к гаранту отправлен",
            time=datetime.now(),
        )
        msg.save()
        return RenderJson({"result": "ok"})
    else:
        if "conf" not in params:
            user = GetCurrentUser(request)
            peer = User.objects.get(id=params.get("peer", 0))
            buyId = params.get("buy", 0)
            saleId = params.get("sale", 0)
            conf = GetOrCreateDialog(GetCurrentUser(request), peer)
            offer = None
            if buyId:
                offer = BuyOffer.objects.get(id=buyId)
            elif saleId:
                offer = SaleOffer.objects.get(id=saleId)
            if offer and CheckConnection(user, offer):
                SendOfferMail(user, offer, conf)
                if type(offer) == BuyOffer:
                    oc = OfferConnection(
                        user=user,
                        buy=offer,
                    )
                else:
                    oc = OfferConnection(
                        user=user,
                        sale=offer,
                    )
                oc.save()
            return redirect("/user/im?conf={}".format(conf.id))
        conf = Conference.objects.get(id=params.get("conf", 0))
        user = GetCurrentUser(request)
        if not conf.users.filter(id=user.id):
            return redirect("/user/mail/")
        return RenderToResponse("user/im.html", request, {
            "conf": conf,
        })

@login_required(login_url="/user/auth/")
@SafeView
def ImMsgFrameView(request):
    params = request.REQUEST
    user = GetCurrentUser(request)
    conf = Conference.objects.get(id=params.get("conf", 0))
    msgs = conf.msgs.all()
    msgs = sorted(msgs, key=lambda self: self.time)
    groups = []
    for msg in msgs:
        if int(params.get("read", True)) and msg.fr != user and msg.new:
            msg.new = False
            msg.save()
        if not groups or groups[-1][0].fr != msg.fr:
            groups.append([])
        groups[-1].append(msg)

    msgs = groups
    return JsonResponse({
        "content": render(request, "user/im_msg_frame.html", {
            "msgs": msgs,
        }).content.decode("utf-8"),
        "opts": {
            "addGuarant": not conf.plusGuarant and not conf.askGuarant,
            "unreadCount": GetUnreadCount(request),
            "toWithGuarant": conf.plusGuarant.url() if conf.plusGuarant and not conf.withGuarant else "",
            "toWithoutGuarant": conf.plusGuarant.url() if conf.plusGuarant and conf.withGuarant else "",
        },
    })


@SafeView
def ProfileView(request, userid=None):
    params = request.REQUEST
    user = User.objects.get(id=userid) if userid else GetCurrentUser(request)
    if not user and not userid:
        return redirect("/user/auth/")
    if not user.visible() and user != GetCurrentUser(request):
        return redirect("/")
    return RenderToResponse("user/profile.html", request, {
        "url": user.profileUrl() if user else "/user/profile/",
        "prUser": user,
        "firsttime": params.get("firsttime", ""),
    })

class FirstnameMissingErr(EditErr):
    def __init__(self):
        super().__init__("firstname_is_missing")

class LastnameMissingErr(EditErr):
    def __init__(self):
        super().__init__("lastname_is_missing")

class InvalidCountryErr(EditErr):
    def __init__(self):
        super().__init__("country_is_invalid")

class BdayMissingErr(EditErr):
    def __init__(self):
        super().__init__("bday_is_missing")

class BdayInvalidErr(EditErr):
    def __init__(self):
        super().__init__("bday_is_invalid")

class OldPassInvalidErr(EditErr):
    def __init__(self):
        super().__init__("old_pass_is_invalid")

class BadPasswordLengthErr(EditErr):
    def __init__(self):
        super().__init__("bad_password_len")

@login_required(login_url="/user/auth/")
@SafeView
def EditProfileView(request):
    params = request.REQUEST
    user = GetCurrentUser(request)
    act = params.get("act", "")
    if user and act == "edit":
        try:
            oldPassw = params.get("oldPassword", "")
            passw = params.get("password", "")
            passw2 = params.get("password2", "")
            if oldPassw or passw or passw2:
                if not authenticate(username=user.username, password=oldPassw):
                    raise OldPassInvalidErr
                if passw != passw2:
                    raise PasswordsAreNotEqualErr
                if not (3 <= len(passw) <= 20):
                    raise BadPasswordLengthErr
                user.set_password(passw)

            if not params.get("firstName", "").strip():
                raise FirstnameMissingErr

            user.first_name = params["firstName"]

            if not params.get("lastName", "").strip():
                raise LastnameMissingErr
            user.last_name = params["lastName"]

            try:
                user.country = Country.objects.get(name=params.get("country", ""))
            except:
                raise InvalidCountryErr

            user.city = params.get("city", "")
            if not params.get("bday", "").strip():
                user.birthday = None
            else:
                try:
                    user.birthday = datetime.strptime(params["bday"], "%d.%m.%Y")
                except ValueError:
                    raise BdayInvalidErr
            user.about = params.get("about", "")

            if 'avatar' in request.FILES:
                StoreImage(request.FILES['avatar'], user.avatar)
                MakeThumbnail(user.avatar, user.avatarThumb)
            user.save()
            return redirect("/user/profile/")
        except EditErr as e:
            raise RedirectExc("/user/edit_profile/?err={}".format(e.status))
        except TsExc as e:
            raise RedirectExc("/user/edit_profile/?err={}".format(str(e)))
    return RenderToResponse("user/edit_profile.html", request, {
        "url": "/user/edit_profile/",
        "prUser": user,
        "countries": GetCountries(),
        "err": GetEditProfileMsg(params.get("err", ""))
    })


@SafeView
def UsersView(request):
    return RenderToResponse("user/list.html", request, {
        "url": "/user/all",
    })

@SafeView
def UsersFilterView(request):
    params = request.REQUEST
    users = User.objects.all()
    users = [ user for user in users if user.visible() ]
    count = int(params.get("count", 30))
    page = int(params.get("page", 0))
    totalpages = (len(users) + count - 1) // count
    block = users[page*count:(page + 1)*count]
    return RenderToResponse("user/filter.html", request, {
        "url": "/user/all",
        "users": users,
        "block": block,
        "page": page,
        "totalpages": totalpages,
        "pagesid": "users"
    })

@login_required(login_url="/user/auth/")
@SafeView
def UserMailView(request):
    user = GetCurrentUser(request)
    confs = Conference.objects.filter(users=user).all()
    confs = [conf for conf in confs if conf.msgs.all()]
    confs.sort(key=lambda conf: conf.msgs.latest("time").time, reverse=True)
    for conf in confs:
        u = conf.users.all()
        conf.peer = u[0] if u[1] == user else u[1]
        conf.msg = conf.msgs.latest("time")
    return RenderToResponse("user/mail.html", request, {
        "url": "/user/mail",
        "confs": confs,
    })


@SafeView
def UserRecoverView(request):
    params = request.REQUEST
    msg = ""
    msgErr = ""
    if request.method == "POST":
        email = params.get("email", "")
        user = User.objects.filter(username=email).all()
        if not user:
            msgErr = "user_does_not_exist"
        else:
            msg = "recover_ok"
            user = user[0]
            newPassword = GetNewId()[0:8]
            user.set_password(newPassword)
            user.save()
            SendRecoverMail(user, newPassword)
    return RenderToResponse("user/recover.html", request, {
        "msg": GetUserRecoverMsg(msg),
        "msgErr": GetUserRecoverMsg(msgErr),
    })
