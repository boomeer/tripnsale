from django.db import models
import tripnsale.settings as settings
from user.models import (
    User,
)

class Backmsg(models.Model):
    name = models.TextField(default="")
    body = models.TextField(default="")
    email = models.TextField(default="")
    user = models.ForeignKey(User, default=None, null=True)
    is_red = models.BooleanField(default=False)
