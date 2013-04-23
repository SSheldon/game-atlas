from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from friends.models import Friends

@login_required
def friend_request_send(request, username):
    if request.method == 'POST':
        friend_id = request.POST['username']
        Friends.add_friends(request.user.id, friend_id)

    return redirect('user:profile')

@login_required
def friend_info(request, friend_id):
    return redirect('user:profile')

@login_required
def friend_request_accept(request):
    if request.method == 'POST':
        accept_friends(request.user.id, request.POST['friends_id'])

    return redirect('user:profile')

@login_required
def friend_request_reject(request):
    if request.method == 'POST':
        reject_friends(Request.user.id, request.POST['friends_id'])
    return redirect('user:profile')

@login_required
def friend_remove(request, username):
    Friends.remove_friends(request.user.id, username)
    return redirect('user:profile', request.user.username)

@login_required
def show_friends(request, username):
    context = {'friends': Friends.get_friends(request.user.id)}

    return render(request, 'friends_list.html', context)


