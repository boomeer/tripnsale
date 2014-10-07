from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext
from user.utils import GetCurrentUser
from util.exc import *


def SafeViewFunc(func, *arg, **argv):
    try:
        return func(*arg, **argv)
    except Exception as e:
        return HttpResponse("Error({}): {}".format(type(e), e))


def SafeView(func):
    return lambda *arg, **argv: SafeViewFunc(func, *arg, **argv)


def RenderToResponse(templPath, request, params):
    params = dict(
        params,
        profileOwner=GetCurrentUser(request),
    )
    return render_to_response(templPath, RequestContext(request, params))


def CheckPost(request):
    if request.method != "POST":
        raise ReqMustBePostErr
