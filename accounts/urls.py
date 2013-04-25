from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^games/$', views.games, name='games'),
    url(r'^games/add/$', 'lists.views.add_game', name='add_game'),
    url(r'^games/recommended/$', 'lists.views.recommended_games', name='recommended_games'),
    url(r'^friends/$', views.friends, name='friends'),
    url(r'^friends/request/$', 'friends.views.friend_request_send', name='request_friend'),
    url(r'^friends/accept/$', 'friends.views.friend_request_accept', name='accept_friend'),
    url(r'^friends/reject/$', 'friends.views.friend_request_reject', name='reject_friend'),
    url(r'^friends/remove/$', 'friends.views.friend_remove', name='remove_friend'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search/games$', views.search_friends_games, name="game_search"),
)
