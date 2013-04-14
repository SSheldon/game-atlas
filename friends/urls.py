from django.conf.urls import patterns, url

from friends import views

urlpatterns = patterns('',
    url(r'^friends/$', views.show_friends),
)
