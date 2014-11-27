from django.shortcuts import HttpResponse, render_to_response, redirect
from django.template import RequestContext
from user.utils import GetCurrentUser
from user.models import Msg
from util.exc import *
from util.msg import *
from util.avatar import *


def SafeViewFunc(func, *arg, **argv):
    try:
        return func(*arg, **argv)
    except RedirectExc as e:
        return redirect(str(e))
    except Exception as e:
        return HttpResponse("Error({}): {}".format(type(e), e))


def SafeView(func):
    return lambda *arg, **argv: SafeViewFunc(func, *arg, **argv)


def RenderToResponse(templPath, request, params):
    user = GetCurrentUser(request)
    unreadCount = Msg.objects.filter(to=user, new=True).count()
    params = dict(
        params,
        profileOwner=GetCurrentUser(request),
        unreadCount=unreadCount,
    )
    return render_to_response(templPath, RequestContext(request, params))


def CheckPost(request):
    if request.method != "POST":
        raise ReqMustBePostErr

