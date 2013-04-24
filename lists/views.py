from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from lists.models import UserGame

def user_games(request, user_id):
    context = {'games': UserGame.get_games(user_id)}
    return render(request, 'lists/games.html', context)

@require_POST
@login_required
def add_game(request, next_page='accounts:games'):
    UserGame.add_game(request.user.id, request.POST['game_id'])
    return redirect(next_page)
