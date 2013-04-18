from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
)
