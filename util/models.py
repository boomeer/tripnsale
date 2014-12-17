from django.db import models


class ContentHolder(models.Model):
    class Meta:
        abstract = True
    title = models.TextField(default="")
    content = models.TextField(default="")
    verified = models.BooleanField(default=True)
