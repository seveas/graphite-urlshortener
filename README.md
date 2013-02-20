Url shortener for graphite
==========================

At the Booking.com hackathon in Ferbuary 2013, I created this workaround for my
biggest annoyance with graphite: the unpasteable urls from hell. Of course it's
possible to use something like tinyurl.com, but I'd rather not make these urls
public.

So, here's a url_shortener that integrates with graphite (it could integrate
with any django app). Once you have one of graphite's humongous URL's, such as
https://graphite.booking.com/render/?[very large list of parameters and names],
simply prepend s/ to the path to create a short url.

Installing
----------
As this is the result of a hackathon, it's a hack to install :)

Add the following to local_settings.py:

    # And now we override som app settings to add the url shortener
    from graphite.app_settings import *
    
    INSTALLED_APPS = INSTALLED_APPS + ('url_shortener',)
    ROOT_URLCONF = 'graphite.local_urls'
    
    # Older versions of graphite-web do a failed attempt to check whether
    # app_settings is loaded (from foo import * does not import attributes
    # starting with an _) So make this detection work with a hack
    import sys
    sys.modules['graphite.settings']._APP_SETTINGS_LOADED = True
    GRAPHITE_WEB_APP_SETTINGS_LOADED = True

Then create local_urls.py and add these contents:
    
    from graphite.urls import *
    urlpatterns = patterns('', ('^s/', include('url_shortener.urls'))) + urlpatterns

Then copy the url_shortener directory over to your python's site-packages
directory (or anywhere else on your $PYTHONPATH. To generate the necessary
create table statement, use this command:

    DJANGO_SETTINGS_MODULE=graphite.settings django-admin sqlall url_shortener

Using it
--------
As said above, simply prepend s/ to any url path to create a short url. I
personally use a javascript bookmarklet for this:

    javascript:window.location.href=window.location.href.replace(/(^https?:..[^/]*)/,%20"$1/s");

And revel in the joy of having shareable graphite links that don't break in
every mail, jabber or irc client.
