from django.contrib import admin
import user.models


admin.site.register(user.models.User)
admin.site.register(user.models.Msg)
