# coding: utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),

    url(r'', include('eventex.core.urls', namespace='core')),
    # url(r'^admin/', include(admin.site.urls)),
)
