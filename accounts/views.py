from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from friends.models import Friend

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Add this user to the database and log them in
            user = form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else: # request.method == 'GET'
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    return redirect('users:profile', request.user.username)

@login_required
def games(request):
    return redirect('users:games', request.user.username)

@login_required
def friends(request):
    return redirect('users:friends', request.user.username)

def search(request):
    context = {}
    if 'user' in request.GET:
        result = User.objects.filter(username__icontains=request.GET['user']) 
        context['users'] = result
    return render(request, 'users/search.html', context)

@login_required
def search_friends_games(request):
    if request.method == 'GET':
        context = {'results': Friend.search_friends_games(request.user.id, request.GET['search'])}
        return render(request, "search_games.html", context)

