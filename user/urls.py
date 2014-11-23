from django.conf.urls import patterns, include, url 
from user.views import *


urlpatterns = patterns('',
    url("^profile/(?P<username>[a-zA-z0-9._-]{1,30})/$", ProfileView),
    url("^profile/$", ProfileView),
    url("^all/$", UsersView),
    url("^auth/$", AuthView),
    url("^mail/$", UserMailView),
    url("^im/$", ImView),
    url("^im_msg_frame/$", ImMsgFrameView),
    url("^logout/$", LogoutView),
)
