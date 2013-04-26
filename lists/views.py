from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from games.models import Game
from lists.models import UserGame
from recommendations.collab_filter import recommend_games
from scrapers.xbox import get_games

@require_POST
@login_required
def add_game(request, next_page='accounts:games'):
    if 'next' in request.POST:
        next_page = request.POST['next']
    UserGame.add_game(request.user.id, request.POST['game_id'])
    return redirect(next_page)

@require_POST
@login_required
def remove_game(request, next_page='accounts:games'):
    if 'next' in request.POST:
        next_page = request.POST['next']
    UserGame.remove_game(request.user.id, request.POST['game_id'])
    return redirect(next_page)

@login_required
def recommended_games(request):
    lists, games = UserGame.get_all_lists()
    recommended_ids = recommend_games(request.user.id, lists, list(games))
    context = {'games_list': Game.select_many(recommended_ids)}
    return render(request, 'games/index.html', context)

@require_POST
@login_required
def import_xbox_games(request):
    titles = get_games(request.POST['gamer_id'])
    games = Game.select_many_by_title(titles)
    game_ids = [game['id'] for game in games]
    UserGame.add_games(request.user.id, game_ids)
    return redirect('accounts:games')
