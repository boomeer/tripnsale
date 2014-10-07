from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tripnsale.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^admin/', include(admin.site.urls)),
    url('^', include('offer.urls')),
    url('^user/', include('user.urls')),
)
