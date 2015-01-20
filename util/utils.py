#-*- coding:utf-8 -*-

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

def _PreprocessWord(w):
    w = w.strip().lower()
    while "  " in w:
        w = w.replace("  ", " ")
    return w

# out is float in [0, 1]. 1 means, words are equals
def _LevenshteinDist(w1, w2, preprocess=False):
    if preprocess:
        w1 = _PreprocessWord(w1)
        w2 = _PreprocessWord(w2)

    # must be: |w1| <= |w2|
    if len(w1) > len(w2):
        w1, w2 = w2, w1

    def __b2i(b):
        return 1 if b else 0

    curD = [ i for i in range(len(w2) + 1) ]
    for i in range(len(w1) + 1):
        prevD, curD = curD, [i]
        for j in range(1, len(w2) + 1):
            curD.append( min(curD[j - 1] + 1, prevD[j] + 1, prevD[j - 1] + __b2i(w1[i] == w2[j])) )

    ldist = curD[-1]
    return 1.0 - ldist / max( len(w1), len(w2) )

def _Translit(w, preprocess=False):
    if preprocess:
        w = _PreprocessWord(w)

    repl = { "а": "a",
             "б": "b",
             "в": "v",
             "г": "g",
             "д": "d",
             "е": "e",
             "ё": "yo",
             "ж": "zh",
             "з": "z",
             "и": "i",
             "й": "i",
             "к": "k",
             "л": "l",
             "м": "m",
             "н": "n",
             "о": "o",
             "п": "p",
             "р": "r",
             "с": "s",
             "т": "t",
             "у": "u",
             "ф": "f",
             "х": "h",
             "ц": "c",
             "ч": "ch",
             "ш": "sh",
             "щ": "sh",
             "ъ": "",
             "ы": "i",
             "ь": "",
             "э": "e",
             "ю": "yu",
             "я": "ya", }
    retw = ""
    for s in w:
        if s in repl:
            retw += repl[s]
        else:
            retw += s
    return ret

def WordDiff(w1, w2, allowTransform=True):
    if not allowTransform:
        return _LevenshteinDist(w1, w2, preprocess=True)
    else:
        w1 = _PreprocessWord(w1)
        w2 = _PreprocessWord(w2)
        res = _LevenshteinDist(w1, w2, preprocess=False)

        if res == 1.0:
            return 1.0

        tw1 = _Translit(w1)
        tw2 = _Translit(w2)

        if tw1 == w1 and tw2 == w2:
            rest = 0.0
        else:
            rest = _LevenshteinDist(tw1, tw2, preprocess=False)

        return max(res, rest)


def ParseBool(text):
    return bool(text.strip()) and text.strip().lower() != "false" and text.strip() != "0"
