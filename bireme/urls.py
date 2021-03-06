from django.conf.urls.defaults import patterns, include, url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# view to redirect from feedback application
def index(request):
    return HttpResponseRedirect(reverse("feedback.views.index"))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bireme.views.home', name='home'),
    # url(r'^bireme/', include('bireme.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    
    url(r'^feedback/', include("feedback.urls")),
    url(r'^$', index),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
