from django.db import models
import django.contrib.auth.models as authModels


class User(authModels.User):
    remoteAddr = models.TextField(default="")
    regRemoteAddr = models.TextField(default="")
    country = models.TextField(default="")
    city = models.TextField(default="")
