from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from friends.models import Friends

@login_required
def friend_request_send(request, username):
    if request.method == 'POST':
        friend_id = request.POST['username']
        Friends.add_friends(user1 = request.user.id,
                            user2 = friend_id)
    
    return redirect('friends:show_friends')

@login_required
def friend_info(request, friend_id):
    return redirect('friends:show_friends')

@login_required
def friend_request_accept(request, friend_id):
    if request.method == 'POST':

        accept_friends(user1 = request.user.id, user2 = request.POST['friends_id'])

    return redirect('friends:show_friends')

@login_required
def friend_request_reject(request):
    if request.method == 'POST':
        reject_friends(user1=request.user.id, 
                        user2 = request.POST['friends_id'])
    return redirect('friends:show_friends')

@login_required
def friend_remove(request, friend_id):
    print 'hey'
    Friends.remove_friends(request.user.id, friend_id)
    return redirect('friends:show_friends')

@login_required
def show_friends(request):
    context = {'friends': Friends.get_friends(request.user.id)}

    return render(request, 'friends_list.html', context)

