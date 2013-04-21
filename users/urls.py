from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    url(r'^(?P<username>[\w.@+-]+)/games/$', views.games),
    url(r'^(?P<username>[\w.@+-]+)/friends/remove/$', views.remove_friend, name="friend_remove")
)
