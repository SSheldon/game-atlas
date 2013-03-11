from django.shortcuts import render

from games.models import Release

def index(request):
    context = {'games_list': Release.select_all()}
    return render(request, 'games.html', context)
