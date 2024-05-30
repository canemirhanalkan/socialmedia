from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from postplatform.models import Posts




def index(request):

    posts = Posts.objects.all().order_by("-date")

    return render(request, "account/index.html", {
        "posts":posts,
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

    user = get_object_or_404(User, pk=user_id)

    return render(request, "account/profile.html", {
        "user":user,
        "posts":posts,
        "user_post":user_post
    })

# def post_delete(request, user_id):
    
#     #user posts
#     posts = Posts.objects.filter(user__id=user_id)
#     user_post = Posts.objects.filter(user__id=user_id)
#     pass

