from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from games.models import Genre, Game, Release

def releases(request):
    context = {'games_list': Release.select_all()}
    return render(request, 'releases.html', context)

def index(request):
    context = {'games_list': Game.select_all()}
    return render(request, 'games/index.html', context)

def game_add(request):
    pass

def game_new(request):
    context = {'genres': Genre.select_all()}
    return render(request, 'games/detail.html', context)

def game_detail(request, game_id):
    context = {'game': Game.select(game_id), 'genres': Genre.select_all()}
    return render(request, 'games/detail.html', context)

def game_edit(request, game_id):
    pass

def game_delete(request, game_id):
    Game.delete(game_id)
    return HttpResponseRedirect(reverse('games:index'))
