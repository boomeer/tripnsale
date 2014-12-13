from django.contrib import admin
from user.models import *


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ("getTitle", "askGuarant", "withGuarant",)


admin.site.register(User)
admin.site.register(Msg)
