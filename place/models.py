from django.db import models
from django.contrib import admin
import tripnsale.settings as settings


class Country(models.Model):
    title = models.TextField(default="")
    ititle = models.TextField(default="")
    name = models.TextField(default="")

    def img(self):
        return "{}/countries/{}_preview.gif".format(settings.STATIC_URL, self.name)

    def __str__(self):
        return self.title

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("title", "ititle", "name")
