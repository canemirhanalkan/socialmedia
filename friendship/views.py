from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Friendship
from .forms import AddFriendForm

@login_required
def add_friend(request, username):

    ##----ayrı bir form da çalıştırmak için----##
    
    # if request.method == 'POST':
    #     form = AddFriendForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         to_user = get_object_or_404(User, username=username)
    #         Friendship.objects.create(from_user=request.user, to_user=to_user)
    #         return redirect('/account/index')
    # else:
    #     form = AddFriendForm()
    # return render(request, 'friendship/add-friend.html', {'form': form})

    to_user = get_object_or_404(User, username=username)
    if not Friendship.objects.filter(from_user=request.user, to_user=to_user).exists():
        Friendship.objects.create(from_user=request.user, to_user=to_user)
    return redirect('/account/index')






@login_required
def friend_list(request):

    #---diğer kullanıcılar
    friends = Friendship.objects.filter(from_user=request.user)
    return render(request, 'friendship/friend-list.html', {'friends': friends})


    #------------------arkadaş olmadığımız kullanıcıları gösterir----------------#
    # current_user = request.user
    # all_users = User.objects.exclude(id=current_user.id)

    # # Kullanıcının eklediği arkadaşları al
    # friends_from = Friendship.objects.filter(from_user=current_user).values_list('to_user', flat=True)
    # # Kullanıcının eklenmiş olduğu arkadaşlık ilişkilerini al
    # friends_to = Friendship.objects.filter(to_user=current_user).values_list('from_user', flat=True)

    # # Tüm arkadaşların id'lerini birleştir
    # friend_ids = set(friends_from).union(set(friends_to))

    # # Arkadaş olmayan kullanıcıları filtrele
    # non_friends = all_users.exclude(id__in=friend_ids)

    # return render(request, 'friendship/friend-list.html', {'users': non_friends})