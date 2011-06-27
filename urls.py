from django.contrib import admin
from django.conf.urls.defaults import *
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maxatronics.views.home', name='home'),
    # url(r'^maxatronics/', include('maxatronics.foo.urls')),    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),    
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
