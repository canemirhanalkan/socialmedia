from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from httpx import post
import requests
import locale
import datetime
from django.http import HttpResponse
from postplatform.models import Posts
from django.utils.text import slugify
from friendship.models import Friendship





def index(request):

#-------------------------weather api-----------------------------#
    city = 'Balıkesir'

    key = '12f9563b5d56a94d23d5c83b004ed158'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':key, 'units':'metric', 'lang':'tr'}
    r = requests.get(url = URL, params=PARAMS)
    res = r.json()

    description = res['weather'][0]['description'].upper()
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    locale.setlocale(locale.LC_ALL,"")
    day = datetime.date.today().strftime("%A")

#----------------------weather api end-----------------------------#



#------------------------------------------------------------------------------------------------------#
    current_user = request.user
    all_users = User.objects.exclude(id=current_user.id)

     # Kullanıcının eklediği arkadaşları al
    friends_from = Friendship.objects.filter(from_user=current_user).values_list('to_user', flat=True)
    # Kullanıcının eklenmiş olduğu arkadaşlık ilişkilerini al
    friends_to = Friendship.objects.filter(to_user=current_user).values_list('from_user', flat=True)

    # Tüm arkadaşların id'lerini birleştir
    friend_ids = set(friends_from).union(set(friends_to))

    # Arkadaş olmayan kullanıcıları filtrele
    non_friends = all_users.exclude(id__in=friend_ids)

#------------------------------------------------------------------------------------------------------#

    friends = Friendship.objects.filter(from_user=request.user)
    users = User.objects.all().order_by("-date_joined")
    posts = Posts.objects.all().order_by("-date")

    if request.user.is_authenticated:
        user_post = Posts.objects.filter(user=request.user)
        posts_count = user_post.count()
    else:
        user_post = None
        posts_count = 0

    return render(request, "account/index.html", {
        'description':description,
        'icon':icon,
        'temp':temp,
        'day':day,
        'city':city,
        'posts':posts,
        'user_post':user_post,
        'posts_count':posts_count,
        'users':users,
        'friends':friends,
        'non_friends':non_friends
    })


#--------USER LOGİN-------------#

def user_login(request):

    if request.user.is_authenticated:
        return redirect("account_index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            nextUrl = request.GET.get("next", None)

            if nextUrl is None:
                return redirect("account_index")
            else:
                return redirect(nextUrl)
        else:
            return render(request, "account/login.html", {"error":"kullanıcı adı ya da parola yanlış"})

    else:
        return render(request, "account/login.html")
    # return render(request, "account/login.html")





#------USER REGİSTER----------#

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        slug = slugify(username)

        if password != password:
            return render(request, "account/register.html", {"error":"Parolalar eşleşmiyor. Yeniden deneyiniz."})
    
        if User.objects.filter(username=username).exists():
            return render(request, "account/register.html", {"error":"Bu kullanıcı adı zaten kullanılıyor."})
                
        if User.objects.filter(email=email).exists():
            return render(request, "account/register.html", {"error":"Bu kullanıcı adı zaten kullanılıyor."})


        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect("user_login")
    
    else:
        return render(request, "account/register.html")


def user_logout(request):
    logout(request)
    return redirect("user_login")


def user_profile(request, user_id):
    
    #user posts
    posts = Posts.objects.filter(user__id=user_id).order_by("-date")
    user_post = Posts.objects.filter(user__id=user_id).order_by("-date")

    #friends
    friends = Friendship.objects.filter(from_user=request.user)

    user = get_object_or_404(User, pk=user_id)

    return render(request, "account/profile.html", {
        "user":user,
        "posts":posts,
        "user_post":user_post,
        "friends":friends,
    })




@login_required()
def post_delete(request, post_id):
    
    post = get_object_or_404(Posts, pk=post_id)

    if post.user == request.user:
        if request.method == "POST":
            post.delete()
            return redirect('account_index')
    else:
        return HttpResponse('bu gönderiyi silmek için yetkiniz yok')

    return render(request, "account/post-delete.html", {
        'post':post
    })