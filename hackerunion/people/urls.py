from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from people.views import *

urlpatterns = patterns('',
    url(r'^$', people_list, name='people_index'),
    #url(r'^signup/$', signup),
    url(r'^(?P<userid>[0-9]+)/$', userid, name='people_userid'),
    url(r'^(?P<username>[A-Za-z0-9]+)/$', profile, name='people_profile'),
)
