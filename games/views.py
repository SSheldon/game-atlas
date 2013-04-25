from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from games.models import Genre, Game, Release
from scrapers.metacritic import get_info

def releases(request):
    context = {'games_list': Release.select_all()}
    return render(request, 'releases.html', context)

def index(request):
    context = {'games_list': Game.select_all()}
    return render(request, 'games/index.html', context)

def game_detail(request, game_id):
    # TODO(ssheldon): Implement a game detail view
    pass

def game_add(request):
    if request.method == 'POST':
        Game.insert(
            title=request.POST['game_title'],
            genre_id=request.POST['genre_id'],
        )
        return redirect('games:index')
    else: # request.method == 'GET'
        context = {'genres': Genre.select_all()}
        return render(request, 'games/edit.html', context)

def game_edit(request, game_id):
    if request.method == 'POST':
        Game.update(game_id,
            title=request.POST['game_title'],
            genre_id=request.POST['genre_id'],
        )
        return redirect('games:index')
    else: # request.method == 'GET'
        context = {'game': Game.select(game_id), 'genres': Genre.select_all()}
        return render(request, 'games/edit.html', context)

@require_POST
def game_delete(request):
    Game.delete(request.POST['game_id'])
    return redirect('games:index')

def game_search(request):
    if request.method == 'GET':
        context = {'games': Game.find(request.GET['title'])}
        return render(request, 'games/search.html', context)

def game_add2(request):
    if request.method == 'POST':
        info_dict = get_info(request.POST['title'], request.POST['platform'])
        if info_dict is None:
            return redirect('games:index')
        Release.game_info(info_dict, request.POST['title'], request.POST['platform'])

    return redirect('games:index')
