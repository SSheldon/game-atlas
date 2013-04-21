from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render

import lists.views as lists_views
import friends.views as friends_views

from friends.models import Friends
from lists.models import UserGame

def games(request, username):
    user = get_object_or_404(User, username=username)
    return lists_views.user_games(request, user.id)

def friends(request, username):
    user = get_object_or_404(User, username=username)
    return friends_views.show_friends(request, user.id)

def remove_friend(request, username):
    user = get_object_or_404(User, username=username)
    return friends_views.friend_remove(request, user.id)

def profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {'friends': Friends.get_friends(user.id), 'games_list': UserGame.get_games(request.user.id), 'page': user}
    return render(request, 'profile1.html', context)
