from django.conf.urls import patterns, include, url
from infos.views import *


urlpatterns = patterns('',
    url("^(?P<name>[A-za-z0-9_-]{1,})/$", InfoView),
)
