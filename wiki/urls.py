from django.conf.urls import patterns, include, url

from django.contrib import admin

from wiki.hello import hello

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', hello),
)
