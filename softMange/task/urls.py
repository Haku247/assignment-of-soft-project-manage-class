"""
urls.py of app
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^home$', views.home, name = 'home'),
    url(r'^me$', views.me, name = 'me'),
    url(r'^publish$', views.publish, name = 'publish'),
    url(r'^receive$', views.receive, name = 'receive'),
    url(r'^receive_get$', views.receive_get, name = 'receive_get'),
    url(r'^published$', views.published, name = 'published'),
    url(r'^complete$', views.complete, name = 'complete'),
    url(r'^received$', views.received, name = 'received'),
    url(r'^received_report$', views.received_report, name = 'received_report'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^signin$', views.signin, name = 'signin'),
    url(r'^log_out$', views.log_out, name = 'log_out'),
    ]