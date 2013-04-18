from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^(?P<username>[\w.@+-]+)/games/$', views.games),
)
