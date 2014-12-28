from django.db import models
import django.contrib.auth.models as authModels
import tripnsale.settings as settings
from datetime import datetime
from place.models import (
    Country,
)
import os


class User(authModels.User):
    remoteAddr = models.TextField(default="")
    regRemoteAddr = models.TextField(default="")
    country = models.ForeignKey(Country)
    city = models.TextField(default="", blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    avatarThumb = models.ImageField(upload_to="avatars/thumbs", blank=True, null=True)
    activated = models.BooleanField(default=True)
    activateCode = models.TextField(default="")
    guarant = models.BooleanField(default=False)
    birthday = models.DateField(default=None, null=True, blank=True)
    about = models.TextField(default="", blank=True)
    hidden = models.BooleanField(default=False)

    def avatarUrl(self):
        return self.avatar.url if self.avatar else "{}/user/av_default.png".format(settings.STATIC_URL)

    def avatarThumbUrl(self):
        return self.avatarThumb.url if self.avatarThumb else "{}/user/av_default.png".format(settings.STATIC_URL)

    def profileUrl(self):
        return "/user/profile/{}/".format(self.id)

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    def visible(self):
        return not self.hidden and not self.guarant


class Msg(models.Model): # DEPRECATED
    fr = models.ForeignKey(User, related_name="user_from")
    to = models.ForeignKey(User, related_name="user_to")
    content = models.TextField()
    time = models.DateTimeField(default=datetime.now())
    new = models.BooleanField(default=True)


class Conference(models.Model):
    title = models.TextField(default="")
    users = models.ManyToManyField(User)
    askGuarant = models.BooleanField(default=False)
    withGuarant = models.BooleanField(default=False)
    plusGuarant = models.ForeignKey("Conference", blank=True, null=True)

    def getTitle(self):
        return ",".join(user.fullname() for user in self.users.all())

    def url(self):
        return "/user/im?conf={}".format(self.id)


class ConferenceMsg(models.Model):
    conf = models.ForeignKey(Conference, related_name="msgs")
    fr = models.ForeignKey(User, blank=True, null=True)
    content = models.TextField(default="")
    time = models.DateTimeField(default=datetime.now())
    new = models.BooleanField(default=True)


class SystemMsg(ConferenceMsg):
    pass
