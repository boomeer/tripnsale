from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from util.utils import (
    SafeView,
    TsExc,
    RedirectExc,
    RenderToResponse,
    CheckPost,
    GetSysMsg,
    StoreImage,
)
from user.models import (
    User,
    Msg,
)
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
import re
from datetime import datetime


class UsernameIsInvalidErr(TsExc):
    def __init__(self):
        super().__init__("username_is_invalid")

class PasswordIsInvalidErr(TsExc):
    def __init__(self):
        super().__init__("password_is_invalid")

class PasswordsAreNotEqualErr(TsExc):
    def __init__(self):
        super().__init__("passwords_are_not_equal")

class MsgCannotBeEmpty(TsExc):
    def __init__(self):
        super().__init__("msg_cannot_be_empty")


@SafeView
def AuthView(request):
    params = request.REQUEST
    act = params.get("act", "")
    if act == "login":
        CheckPost(request)
        user = authenticate(
            username=params.get("login", ""),
            password=params.get("password", ""),
        )
        if user:
            user.remoteAddr = request.META["REMOTE_ADDR"]
            user.save()
            login(request, user)
        else:
            raise RedirectExc("/user/auth/?msgLogin=wrong_login_or_password")
        backref = params.get("backref", "/")
        if not backref:
            backref = "/"
        return redirect(backref)
    elif act == "reg":
        CheckPost(request)
        if params["password"] != params["password2"]:
            raise PasswordsAreNotEqualErr
        if not re.compile("^[a-zA-Z0-9._-]{3,30}$").match(params["username"]):
            raise UsernameIsInvalidErr
        if not re.compile("^.{3,30}$").match(params["password"]):
            raise PasswordIsIvalidErr
        country = Country.objects.get(name=params.get("country", 0))
        user = User.objects.create_user(
            params.get("username", ""),
            params.get("email", ""),
            params.get("password", ""),
            first_name=params.get("firstName", ""),
            last_name=params.get("lastName", ""),
            country=country,
            city=params.get("city", ""),
            remoteAddr=request.META["REMOTE_ADDR"],
            regRemoteAddr=request.META["REMOTE_ADDR"],
        )
        user.save()
        user = authenticate(
            username=user.username,
            password=params.get("password", ""),
        )
        login(request, user)
        return redirect("/")
    return RenderToResponse("user/auth.html", request, {
        "countries": GetCountries(),
        "msgLogin": GetSysMsg(params.get("msgLogin", "")),
        "msgReg": GetSysMsg(params.get("msgReg", "")),
    })


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
        peer = User.objects.get(id=params.get("peer", 0))
        user = GetCurrentUser(request)
        content = params.get("content", "").strip()
        if not content:
            raise MsgCannotbeEmptyErr
        msg = Msg(
            fr=user,
            to=peer,
            content=content,
            time=datetime.now(),
        )
        msg.save()
        return RenderJson({"result": "ok"})
    else:
        peer = User.objects.get(id=params.get("peer", 0))
        return RenderToResponse("user/im.html", request, {
            "peer": peer,
        })


@SafeView
def ImMsgFrameView(request):
    params = request.REQUEST
    peer = User.objects.get(id=params.get("peer", 0))
    user = GetCurrentUser(request)
    msgs = list(Msg.objects.filter(fr=user, to=peer).all()) + \
        list(Msg.objects.filter(fr=peer, to=user).all())
    msgs = sorted(msgs, key=lambda self: self.time)
    groups = []
    for msg in msgs:
        if msg.to == user and msg.new:
            msg.new = False
            msg.save()
        if not groups or groups[-1][0].fr != msg.fr:
            groups.append([])
        groups[-1].append(msg)

    msgs = groups
    return RenderToResponse("user/im_msg_frame.html", request, {
        "peer": peer,
        "msgs": msgs,
    })


@SafeView
def ProfileView(request, username=None):
    params = request.REQUEST
    user = User.objects.get(username=username) if username else GetCurrentUser(request)
    if not user and not username:
        return redirect("/user/auth/")
    return RenderToResponse("user/profile.html", request, {
        "url": "/user/profile/{}".format(user.username) if user else "/user/profile/",
        "prUser": user,
    })


@login_required(login_url="/user/auth/")
@SafeView
def EditProfileView(request):
    params = request.REQUEST
    user = GetCurrentUser(request)
    act = params.get("act", "")
    if user and act == "edit":
        oldPassw = params.get("oldPassword", "")
        passw = params.get("password", "")
        passw2 = params.get("password2", "")
        if oldPassw or passw or passw2:
            if not authenticate(username=user.username, password=oldPassw):
                raise Exception("wrong_old_password")
            if passw != passw2:
                raise Exception("passwords_are_not_equal")
            user.set_password(passw)
        user.first_name = params.get("firstName", "")
        user.last_name = params.get("lastName", "")
        user.country = Country.objects.get(name=params.get("country", ""))
        user.city = params.get("city", "")
        if 'avatar' in request.FILES:
            StoreImage(request.FILES['avatar'], user.avatar, user.username)
        user.save()
        return redirect("/user/profile/")
    return RenderToResponse("user/edit_profile.html", request, {
        "url": "/user/edit_profile/",
        "prUser": user,
        "countries": GetCountries(),
    })
    

@SafeView
def UsersView(request):
    users = User.objects.all()
    return RenderToResponse("user/list.html", request, {
        "url": "/user/all",
        "users": users,
    })


@SafeView
def UserMailView(request):
    user = GetCurrentUser(request)
    msgs = list(Msg.objects.filter(fr=user).all()) + \
            list(Msg.objects.filter(to=user).all())
    lastMsg = {}
    for msg in msgs:
        peer = msg.fr if msg.to == user else msg.to
        last = lastMsg.get(peer, None)
        if not last or last.time < msg.time:
            lastMsg[peer] = msg
    dialogs = [{
        "peer": peer,
        "msg": msg,
    } for peer, msg in lastMsg.items()]
    dialogs = sorted(dialogs, key=lambda self: self["msg"].time)
    dialogs.reverse()
    return RenderToResponse("user/mail.html", request, {
        "url": "/user/mail",
        "dialogs": dialogs,
    })
