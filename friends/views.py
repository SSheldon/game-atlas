from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from friends.models import Friend

@login_required
def friend_request_send(request):
    if request.method == 'POST':
        friend_id = request.POST['friend_id']
        Friend.add_friends(request.user.id, friend_id)

    return redirect('accounts:profile')

@login_required
def friend_info(request, friend_id):
    return redirect('accounts:profile')

@login_required
def friend_request_accept(request):
    if request.method == 'POST':
        Friend.accept_friends(request.user.id, request.POST['friend_id'])

    return redirect('accounts:profile')

@login_required
def friend_request_reject(request):
    if request.method == 'POST':
        Friend.reject_friend(request.user.id, request.POST['friend_id'])
    return redirect('accounts:profile')

@require_POST
@login_required
def friend_remove(request):
    Friend.remove_friends(request.user.id, request.POST['friend_id'])
    return redirect('accounts:profile')

@login_required
def show_friends(request, username):
    context = {'friends': Friend.get_friends(request.user.id)}

    return render(request, 'friends_list.html', context)


@login_required
def show_pending_friends(request, username):
    context = {'pending_friends': Friend.get_pending_friends(request.user.id)}

    return render(request, 'pending_friends', context)

