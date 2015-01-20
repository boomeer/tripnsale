from django.contrib import admin
from user.models import *


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ("getTitle", "askGuarant", "withGuarant",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "country",
                    "city", "activated", "guarant", "hidden", "emailNotify",)


@admin.register(ConferenceMsg)
class ConferenceMsgAdmin(admin.ModelAdmin):
    list_display = ("content", "conf", "fr", "time", "new", "notified",)
    list_filter = ("conf", "fr",)
