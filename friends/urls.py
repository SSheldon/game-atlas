from django.conf.urls import patterns, url

from friends import views

urlpatterns = patterns('',
    url(r'^list/$', views.show_friends),
    url(r'^(?P<friend_id>\d+)/remove/$', views.friend_remove, name='friend_remove'),
)
