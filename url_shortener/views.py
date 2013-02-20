from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect

from url_shortener.baseconv import base62
from url_shortener.models import Link

def follow(request, base62_id):
    """ 
    View which gets the link for the given base62_id value
    and redirects to it.
    """
    if request.META.get('QUERY_STRING', None):
        return create(request, base62_id + '/')
    key = base62.to_decimal(base62_id)
    link = get_object_or_404(Link, pk=key)
    return HttpResponsePermanentRedirect('/' + link.url)

def create(request, path):
    if request.META.get('QUERY_STRING', None):
        path += '?' + request.META['QUERY_STRING']
    new_link, created = Link.objects.get_or_create(url=path)
    link = new_link.to_base62()
    return HttpResponse("Your short link is <a href=\"/s/%s\">/s/%s</a>" % (link, link))
