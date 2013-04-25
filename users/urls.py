from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    url(r'^(?P<username>[\w.@+-]+)/games/$', views.games, name='games'),
    url(r'^(?P<username>[\w.@+-]+)/friends/remove/$', views.remove_friend, name="remove_friend"),
    url(r'^(?P<username>[\w.@+-]+)/friends/accept/$', views.accept_friend, name="accept_friend"),
    url(r'^(?P<username>[\w.@+-]+)/friends/reject/$', views.reject_friend, name="reject_friend"),
    url(r'^(?P<username>[\w.@+-]+)/friends/send/$', views.send_friend_request, name="send_friend_request"),
)
