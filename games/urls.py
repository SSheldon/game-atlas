from django.conf.urls import patterns, url

from games import views

urlpatterns = patterns('',
    url(r'^$', views.releases, name='releases'),
    url(r'^(?P<game_id>\d+)/delete/$', views.game_delete, name='game_delete'),
)
