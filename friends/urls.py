from django.conf.urls import patterns, url

from friends import views

urlpatterns = patterns('',
    url(r'^$', views.show_friends, name='show_friends'),
    url(r'^/(?P<friend_id>\d+)/', views.friend_info, name='friend_info'),
    url(r'^(?P<friend_id>\d+)/remove/$', views.friend_remove, name='friend_remove'),
)
