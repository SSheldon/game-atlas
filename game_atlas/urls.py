from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game_atlas.views.home', name='home'),
    # url(r'^game_atlas/', include('game_atlas.foo.urls')),

    url(r'^$', 'games.views.index', name='home'),
    url(r'^games/', include('games.urls', namespace='games')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^users/', include('users.urls', namespace='users')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
