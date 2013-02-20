from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<base62_id>[a-zA-Z0-9]+)/?$', 'url_shortener.views.follow'),
    (r'^(?P<path>.*)$', 'url_shortener.views.create'),
)
