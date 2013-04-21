from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

import lists.views as lists_views
import friends.views as friends_views

def games(request, username):
    user = get_object_or_404(User, username=username)
    return lists_views.user_games(request, user.id)

def friends(request, username):
    user = get_object_or_404(User, username=username)
    return friends_views.show_friends(request, user.id)

def remove_friend(request, username):
    user = get_object_or_404(User, username=username)
    return friends_views.friend_remove(request, user.id)