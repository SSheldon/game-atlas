from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

@login_required
def profile(request):
    return HttpResponse("You have successfully logged in.")

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
