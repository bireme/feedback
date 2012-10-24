from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^(?P<software>\d+)/?$', "feedback.views.first"),
    (r'^second/(?P<feedback>\d+)/?$', 'feedback.views.second'),
)
