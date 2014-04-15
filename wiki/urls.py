from django.conf.urls import patterns, include, url

from django.contrib import admin

from wiki.hello import hello

from wiki.current_datetime import current_datetime

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', hello),
    url(r'^time/$', current_datetime)
)
