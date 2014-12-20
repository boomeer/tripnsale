from django.conf.urls import patterns, include, url 
from gallery.views import *


urlpatterns = patterns('',
    url("^add_photo/$", GalleryAddPhotoView),
)
