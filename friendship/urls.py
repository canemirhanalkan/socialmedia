from django.urls import path, include
from . import views

app_name = 'friendship'


urlpatterns = [
    path('add-friend/<str:username>', views.add_friend, name='add_friend'),
    path('friend-list/', views.friend_list, name='friend_list'),
]