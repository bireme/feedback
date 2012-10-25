from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    
    url(r'^form/(?P<software>\d+)/?$', "feedback.views.first"),
    url(r'^aditional-information/(?P<feedback>\d+)/?$', 'feedback.views.second'),
    url(r'^thanks/?$', direct_to_template, {'template': 'feedback/thanks.html'}, name="feedback_thanks"),
    url(r'^$', "feedback.views.index"),
)
