from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from friends.models import Friends
from accounts import views

@login_required
def friend_request_send(request, username):
    pass
@login_required
def friend_request_accept(request):
    pass
@login_required
def friend_request_reject(request):
    pass
@login_required
def friend_remove(request, friend_id):
    pass

