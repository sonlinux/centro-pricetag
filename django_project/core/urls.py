    # coding=utf-8
"""Project level url handler."""
from __future__ import absolute_import

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseServerError
from django.template import loader, Context
from rest_framework_swagger.views import get_swagger_view
from contactus import urls as contact_urls

admin.autodiscover()
handler404 = 'base.viewsets.error_views.custom_404'


def handler500(request):
    """500 error handler which includes ``request`` in the context.

    See http://raven.readthedocs.org/en/latest/integrations/
        django.html#message-references

    :param request: Django request object.

    Templates: `500.html`
    Context: None
    """
    # You need to create a 500.html template.
    t = loader.get_template('500.html')
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))

urlpatterns = [
    url(r'^', include('content.urls', namespace='content')),
    url('^contact/', include(contact_urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^site-admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^tracking/', include('tracking.urls')),
    url(r'^accounts/', include('allauth.urls')),
]

admin.site.site_header = 'Pricetag website Admin'
admin.site.site_title = 'Pricetag website Admin'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
