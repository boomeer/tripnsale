from django.db import models
import tripnsale.settings as settings


class Country(models.Model):
    title = models.TextField(default="")
    ititle = models.TextField(default="")
    name = models.TextField(default="")
    order = models.IntegerField(default=0)

    def img(self):
        return "{}/countries/{}_preview.gif".format(settings.STATIC_URL, self.name)

    def __str__(self):
        return self.title

