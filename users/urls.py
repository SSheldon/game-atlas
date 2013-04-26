from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    url(r'^(?P<username>[\w.@+-]+)/games/$', views.games, name='games'),
    url(r'^(?P<username>[\w.@+-]+)/friends/$', views.friends, name='friends'),
)
