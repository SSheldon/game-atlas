from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    url(r'^friends/$', views.friends, name='friends'),
)
