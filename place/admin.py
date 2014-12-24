from django.contrib import admin
from place.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("title", "ititle", "name", "order",)
    list_editable = ("order",)
