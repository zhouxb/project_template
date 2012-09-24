from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import MEDIA_ROOT, STATIC_ROOT, HEROKU

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if HEROKU:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    )
else:
    urlpatterns += staticfiles_urlpatterns()

