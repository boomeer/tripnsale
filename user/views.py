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
)
import re


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


@SafeView
def ProfileView(request):
    return render_to_response("user/profile.html", RequestContext(request, {
    }))


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
        return redirect("/")
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
    return redirect("/")
