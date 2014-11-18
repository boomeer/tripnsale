from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from util.utils import (
    SafeView,
    TsExc,
    RenderToResponse,
    CheckPost,
)
from user.models import (
    User,
    Msg,
)
from user.utils import (
    GetCurrentUser,
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

class IncorrectUsernameOrPasswordErr(TsExc):
    def __init__(self):
        super().__init__("incorrect_username_or_password")

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
            raise IncorrectUsernameOrPasswordErr
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
        user = User.objects.create_user(
            params.get("username", ""),
            params.get("email", ""),
            params.get("password", ""),
            first_name=params.get("firstName", ""),
            last_name=params.get("lastName", ""),
            country=params.get("country", ""),
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
    })


@SafeView
def LogoutView(request):
    logout(request)
    backref = request.REQUEST.get("backref", "/")
    if not backref:
        backref = "/"
    return redirect(backref)


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
        if msg.new:
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
    return RenderToResponse("user/profile.html", request, {
        "url": "/user/profile{}".format(user.username),
        "prUser": user,
    })

@SafeView
def UsersView(request):
    user = User.objects.all()
    return RenderToResponse("user/list.html", request, {
        "url": "user/all",
        "users": User.objects.all()
    })
