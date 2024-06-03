import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import requests
import locale
from .models import Posts, Like
from django.contrib.auth.models import User
from postplatform.forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from friendship.models import Friendship
# Create your views here.


def index(request):

#-----------------WEATHER APİ--------------------------------#
    # city = 'Samsun'

    # key = '12f9563b5d56a94d23d5c83b004ed158'
    # URL = 'https://api.openweathermap.org/data/2.5/weather'
    # PARAMS = {'q':city, 'appid':key, 'units':'metric', 'lang':'tr'}
    # r = requests.get(url = URL, params=PARAMS)
    # res = r.json()

    # description = res['weather'][0]['description'].upper()
    # icon = res['weather'][0]['icon']
    # temp = res['main']['temp']

    # locale.setlocale(locale.LC_ALL,"")
    # day = datetime.date.today().strftime("%A")
#-----------------WEATHER APİ END-----------------------------#



#-----------------Posts Objects-----------------------------#
    posts = Posts.objects.all().order_by("-date")



    return render(request, 'postplatform/index.html', {
        # 'description':description,
        # 'icon':icon,
        # 'temp':temp,
        # 'day':day,
        # 'city':city,
        'posts':posts,
    })



##------------------ POST DETAİL PAGE ----------------------##
def post_detail(request, post_id):

    post = get_object_or_404(Posts, pk=post_id)


    return render(request, 'postplatform/postdetail.html', {
        'post':post,
    })



##-------------- CREATE POST ------------------------------##
@login_required()
def create_post(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/account/index')
    else:
        form = PostCreateForm()
    return render(request, 'postplatform/createpost.html',{
        "form":form
    })



#-----------profile view-------------##
def profile_view(request, user_id):

    profile_user = get_object_or_404(User, id=user_id)
    posts = Posts.objects.filter(user=profile_user)

    friends = Friendship.objects.filter(from_user=user_id)


    return render(request, "postplatform/profileview.html", {
        'profile_user': profile_user,
        'posts':posts,
        'friends':friends,
    })



#------------post like------------------#

def like_post(request):
    user = request.user
    referer = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Posts.objects.get(id=post_id)
        

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

        if referer:
            return HttpResponseRedirect(referer)
        else:
            return HttpResponseRedirect(reverse('account_index'))
