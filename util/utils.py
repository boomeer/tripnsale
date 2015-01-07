from django.shortcuts import HttpResponse, render_to_response, redirect
from django.template import RequestContext
from user.utils import GetCurrentUser, GetUnreadCount
from user.models import Msg
from util.exc import *
from util.msg import *
from valute.models import Valute
from datetime import datetime
from django.utils.html import escape
import tripnsale.settings as settings

import string
import random


def SafeViewFunc(func, *arg, **argv):
    try:
        return func(*arg, **argv)
    except RedirectExc as e:
        return redirect(str(e))
    except Exception as e:
        if not settings.DEBUG:
            return HttpResponse(escape("Error({}): {}".format(type(e), e)))
        raise e


def SafeView(func):
    return lambda *arg, **argv: SafeViewFunc(func, *arg, **argv)


def RenderToResponse(templPath, request, params):
    user = GetCurrentUser(request)
    unreadCount = GetUnreadCount(request)
    usdcourse = Valute.objects.filter(fromId__exact="USD")[0]
    eurocourse = Valute.objects.filter(fromId__exact="EUR")[0]

    params = dict(
        params,
        profileOwner=GetCurrentUser(request),
        unreadCount=unreadCount,
        usdCourse=usdcourse,
        euroCourse=eurocourse,
        now=datetime.now(),
    )
    return render_to_response(templPath, RequestContext(request, params))


def CheckPost(request):
    if request.method != "POST":
        raise ReqMustBePostErr


def GetNewId():
    newId = ''.join(random.choice(string.ascii_lowercase \
        + string.digits) for i in range(20))
    return newId


def ValidFilter(text, filt):
    wt = text.split()
    wf = filt.split()
    for w in wf:
        w = w.lower()
        ok = False
        for ww in wt:
            ww = ww.lower()
            eq = len(w) <= len(ww) and ww[:len(w)] == w
            ok = ok or eq
        if not ok:
            return False
    return True
