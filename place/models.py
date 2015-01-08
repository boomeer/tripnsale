from django.db import models
import tripnsale.settings as settings
import os.path

class Country(models.Model):
    title = models.TextField(default="")
    ititle = models.TextField(default="")
    name = models.TextField(default="")
    order = models.IntegerField(default=0)

    def img(self):
        return os.path.join(settings.STATIC_URL, "countries/{}_preview.gif".format(self.name))

    def __str__(self):
        return self.title

