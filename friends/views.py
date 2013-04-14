from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from friends.models import Friends

@login_required
def friend_request_send(request, username):
    pass

@login_required
def friend_request_accept(request):
    pass

@login_required
def friend_request_reject(request):
    pass

@login_required
def friend_remove(request, friend_id):
    Friends.remove_friends(request.user.id, friend_id)

    return redirect('friends:list')

@login_required
def show_friends(request):
	context = {'friends': Friends.get_friends(request.user.id)}

	return render(request, 'friends_list.html', context)

