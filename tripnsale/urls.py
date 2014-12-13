from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import tripnsale.settings as settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tripnsale.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^admin/', include(admin.site.urls)),
    url('^', include('main.urls')),
    url('^offer/', include('offer.urls')),
    url('^user/', include('user.urls')),
    url('^guarant/', include('guarant.urls')),
    url('^info/', include('infos.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
