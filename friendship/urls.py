from django.urls import path, include
from . import views

urlpatterns = [
    path('add-friend/', views.add_friend, name='add_friend'),
    path('friend-list/', views.friend_list, name='friend_list'),
]