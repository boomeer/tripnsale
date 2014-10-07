from django.db import models


class ContentHolder(models.Model):
    class Meta:
        abstract = True
    title = models.TextField(default="")
    content = models.TextField(default="")
    visible = models.BooleanField(default=True)
    verified = models.BooleanField(default=True)
