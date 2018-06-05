"""
Definition of urls for softMange.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from task.views import home

urlpatterns = [
    # Examples:
    #url(r'^$', softMange.views.home, name='home'),
    # url(r'^softMange/', include('softMange.softMange.urls')),
    url(r'^$', home, name = 'home'),
    url(r'', include('task.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]
