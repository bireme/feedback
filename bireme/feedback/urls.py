from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    
    url(r'^(?P<software>[\w_-]+)/?$', 'feedback.views.first'),
    url(r'^aditional-information/(?P<feedback>\d+)/?$', 'feedback.views.second', name="feedback_second"),
    url(r'^thanks/(?P<feedback>\d+)/?$', 'feedback.views.thanks', name="feedback_thanks"),
    url(r'^thanks2/(?P<feedback>\d+)/?$', 'feedback.views.thanks2', name="feedback_thanks2"),
    url(r'^$', "feedback.views.index"),
)
