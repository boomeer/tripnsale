from django.conf.urls import patterns, include, url
from user.views import *


urlpatterns = patterns('',
    url("^profile/(?P<userid>[0-9]+)/$", ProfileView),
    url("^profile/$", ProfileView),
    url("^edit_profile/$", EditProfileView),
    url("^all/$", UsersView),
    url("^auth/$", AuthView),
    url("^activate/(?P<code>[a-z0-9]{20,20})/$", ActivateView),
    url("^mail/$", UserMailView),
    url("^im/$", ImView),
    url("^im_msg_frame/$", ImMsgFrameView),
    url("^logout/$", LogoutView),
)
