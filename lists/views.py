from django.shortcuts import render

from lists.models import UserGame

def user_games(request, user_id):
    context = {'games_list': UserGame.get_games(user_id)}
    return render(request, 'games/index.html', context)
