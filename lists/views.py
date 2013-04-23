from django.shortcuts import render

from lists.models import UserGame

def user_games(request, user_id):
    context = {'games': UserGame.get_games(user_id)}
    return render(request, 'lists/games.html', context)
