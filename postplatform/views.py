import datetime
from django.shortcuts import get_object_or_404, redirect, render
import requests
import locale
from .models import Posts
from postplatform.forms import PostCreateForm
from django.contrib.auth.decorators import login_required

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
        'post':post
    })



##-------------- CREATE POST ------------------------------##
@login_required()
def create_post(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/posts')
    else:
        form = PostCreateForm()
    return render(request, 'postplatform/createpost.html',{
        "form":form
    })





