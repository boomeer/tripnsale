from django.db import models
from django.contrib import admin

class Country(models.Model):
    title = models.TextField(default="")
    ititle = models.TextField(default="")
    name = models.TextField(default="")

    def __str__(self):
        return self.title

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("title", "ititle", "name")
