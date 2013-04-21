from django.conf.urls import patterns, url, include

from users import views

urlpatterns = patterns('',
    url(r'^(?P<username>[\w.@+-]+)/games/$', views.games),
    url(r'^(?P<username>[\w.@+-]+)/friends/$', views.friends, name='show_friends'),
    url(r'^(?P<username>[\w.@+-]+)/friends/remove/$', views.remove_friend, name="friend_remove")
)
