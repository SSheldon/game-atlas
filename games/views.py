from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from games.models import Game, Release

def releases(request):
    context = {'games_list': Release.select_all()}
    return render(request, 'releases.html', context)

def game_delete(request, game_id):
    Game.delete(game_id)
    return HttpResponseRedirect(reverse('games:index'))
