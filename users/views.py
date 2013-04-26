from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render

import friends.views as friends_views

from friends.models import Friend
from lists.models import UserGame

def games(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'games': UserGame.get_games(user.id),
        'profile': user,
    }
    return render(request, 'users/games.html', context)

def friends(request, username):
    user = get_object_or_404(User, username=username)
    return friends_views.show_friends(request, user.id)

def profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'friends': Friend.get_friends(user.id),
        'games': UserGame.get_games(user.id),
        'profile': user,
        'pending_friends': Friend.get_pending_friends(user.id),
    }

    return render(request, 'users/profile.html', context)

