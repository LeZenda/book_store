from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin

from urlparse import urlparse
import json
import sys

from statistic import models


def dumps(value):
    return json.dumps(value, default=lambda o: None)


class WebRequestMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        setattr(request, 'hide_post', view_kwargs.pop('hide_post', False))

    def process_response(self, request, response):

        if request.path.endswith('/favicon.ico') or request.path.startswith('/admin'):
            return response

        if type(response) == HttpResponsePermanentRedirect and settings.APPEND_SLASH:
            new_location = response.get('location', None)
            content_length = response.get('content-length', None)

            if new_location and content_length is '0':
                new_parsed = urlparse(new_location)

                old = (('http', 'https')[request.is_secure()], request.get_host(),
                       '{0}/'.format(request.path), request.META['QUERY_STRING'])
                new = (new_parsed.scheme, new_parsed.netloc, new_parsed.path, new_parsed.query)

                if old == new:
                    return response
        try:
            self.save(request, response)
        except Exception as e:
            print >> sys.stderr, "Error saving request log", e

        return response

    def save(self, request, response):
        if hasattr(request, 'user') and request.user.is_authenticated():
            user = request.user
        else:
            user = None

        meta = request.META.copy()
        meta.pop('QUERY_STRING', None)
        meta.pop('HTTP_COOKIE', None)
        remote_addr_fwd = None

        if 'HTTP_X_FORWARDED_FOR' in meta:
            remote_addr_fwd = meta['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
            if remote_addr_fwd == meta['HTTP_X_FORWARDED_FOR']:
                meta.pop('HTTP_X_FORWARDED_FOR')

        models.RequestSat(
            host=request.get_host(),
            path=request.path,
            method=request.method,
            uri=request.build_absolute_uri(),
            status_code=response.status_code,
            user_agent=meta.pop('HTTP_USER_AGENT', None),
            remote_addr=meta.pop('REMOTE_ADDR', None),
            remote_addr_fwd=remote_addr_fwd,
            meta=None if not meta else dumps(meta),
            cookies=None if not request.COOKIES else dumps(request.COOKIES),
            is_secure=request.is_secure(),
            is_ajax=request.is_ajax(),
            user=user
        ).save()
