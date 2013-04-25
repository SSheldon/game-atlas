from django.conf.urls import patterns, url

from games import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^releases/$', views.releases, name='releases'),
    url(r'^add/$', views.game_add, name='game_add'),
    url(r'^add2/$', views.game_add2, name='game_add2'),
    url(r'^delete/$', views.game_delete, name='game_delete'),
    url(r'^search/$', views.game_search, name='game_search'),
    url(r'^(?P<game_id>\d+)/$', views.game_detail, name='game_detail'),
    url(r'^(?P<game_id>\d+)/edit/$', views.game_edit, name='game_edit'),
)
