from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from friends.models import Friends

def friend_request_send(request):
    pass
def friend_request_accept(request):
    pass
def friend_request_reject(request):
    pass
def friend_remove(request):
    pass
