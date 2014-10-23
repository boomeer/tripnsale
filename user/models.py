from django.db import models
import django.contrib.auth.models as authModels
import tripnsale.settings as settings


class User(authModels.User):
    remoteAddr = models.TextField(default="")
    regRemoteAddr = models.TextField(default="")
    country = models.TextField(default="")
    city = models.TextField(default="")
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)

    def avatarUrl(self):
        return self.avatar.url if self.avatar else "{}/user/av_default.png".format(settings.STATIC_URL)
