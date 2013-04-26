from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from lists.models import UserGame
from recommendations.collab_filter import recommend_games

def user_games(request, user_id):
    context = {'games': UserGame.get_games(user_id)}
    return render(request, 'lists/games.html', context)

@require_POST
@login_required
def add_game(request, next_page='accounts:games'):
    UserGame.add_game(request.user.id, request.POST['game_id'])
    return redirect(next_page)

@require_POST
@login_required
def remove_game(request, next_page='accounts:games'):
    UserGame.remove_game(request.user.id, request.POST['game_id'])
    return redirect(next_page)

@login_required
def recommended_games(request):
    lists, games = UserGame.get_all_lists()
    recommended = recommend_games(request.user.id, lists, list(games))
    return HttpResponse(str(recommended))
