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
    city = models.TextField(default="")
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    activated = models.BooleanField(default=True)
    activateCode = models.TextField(default="")

    def avatarUrl(self):
        return self.avatar.url if self.avatar else "{}/user/av_default.png".format(settings.STATIC_URL)

    def profileUrl(self):
        return "/user/profile/{}/".format(self.username)


class Msg(models.Model):
    fr = models.ForeignKey(User, related_name="user_from")
    to = models.ForeignKey(User, related_name="user_to")
    content = models.TextField()
    time = models.DateTimeField(default=datetime.now())
    new = models.BooleanField(default=True)
