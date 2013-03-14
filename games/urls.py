from django.conf.urls import patterns, url

from games import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.game_add, name='game_add'),
    url(r'^(?P<game_id>\d+)/$', views.game_detail, name='game_detail'),
    url(r'^(?P<game_id>\d+)/edit/$', views.game_edit, name='game_edit'),
    url(r'^(?P<game_id>\d+)/delete/$', views.game_delete, name='game_delete'),
)
