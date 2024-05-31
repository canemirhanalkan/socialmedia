from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Friendship
from .forms import AddFriendForm

@login_required
def add_friend(request):
    if request.method == 'POST':
        form = AddFriendForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            to_user = get_object_or_404(User, username=username)
            Friendship.objects.create(from_user=request.user, to_user=to_user)
            return redirect('friend_list')
    else:
        form = AddFriendForm()
    return render(request, 'friendship/add-friend.html', {'form': form})

@login_required
def friend_list(request):
    friends = Friendship.objects.filter(from_user=request.user)
    return render(request, 'friendship/friend-list.html', {'friends': friends})
