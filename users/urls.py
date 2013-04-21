from django.conf.urls import patterns, url, include

from users import views

urlpatterns = patterns('',
    url(r'^(?P<username>[\w.@+-]+)/games/$', views.games),
    url(r'^(?P<username>[\w.@+-]+)/friends/$', views.friends, name='show_friends'),
)
