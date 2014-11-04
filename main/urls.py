from django.conf.urls import patterns, include, url 
from main.views import *


urlpatterns = patterns('',
    url("^$", MainView),
)
