from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^profile/$', views.profile, name='profile'),
)
