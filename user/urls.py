from django.conf.urls import patterns, include, url 
from user.views import *


urlpatterns = patterns('',
    url("^profile/(?P<username>[a-zA-z0-9._-]{1,30})/$", ProfileView),
    url("^auth/$", AuthView),
    url("^logout/$", LogoutView),
)
