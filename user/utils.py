from user.models import *
from util.exc import TsExc
from django.contrib.auth.models import User as djUser
from django.shortcuts import render
from django.template.loader import render_to_string
from mail.utils import (
    SendMail,
)


class AuthErr(TsExc):
    def __init__(self):
        super().__init__("auth_err")


def GetUserByDjUser(djUser):
    userId = djUser.id if djUser and djUser.is_authenticated() else None
    users = User.objects.filter(id=userId).all()
    return users[0] if users else None


def GetDjUserByUser(user):
    userId = user.id if user else None
    users = djUser.objects.filter(id=userId).all()
    return users[0] if users else None


def GetCurrentUser(request):
    return GetUserByDjUser(request.user)


def CheckAuth(request):
    if not GetCurrentUser(request):
        raise AuthErr


def SendActivateMail(user):
    content = render_to_string("mail/activate.html", {
        "user": user,
        "hostAddr": settings.CURRENT_HOST,
    })
    SendMail("activate@tripnsale.com", user.email, content)
    

def CreateDialog(fr, to):
    conf = Conference()
    conf.save()
    conf.users.add(fr, to)
    return conf

def GetOrCreateDialog(fr, to):
    confs = Conference.objects.filter(users=fr).all()
    confs = [conf for conf in confs if to in conf.users.all()]
    conf = confs[0] if confs else CreateDialog(fr, to)
    return conf


def GetUnreadCount(request):
    user = GetCurrentUser(request)
    unread = ConferenceMsg.objects.filter(conf__users=user, new=True).exclude(fr=user).count()
    return unread
