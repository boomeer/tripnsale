from django.conf.urls import patterns, include, url
from guarant.views import *


urlpatterns = patterns('',
    url("^asks/$", AsksView),
    url("^accept/(?P<confId>[0-9]{1,})/$", AcceptView),
)
