from django.contrib import admin
from gallery.models import *


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("img", "gallery",)
