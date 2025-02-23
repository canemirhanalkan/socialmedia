from django.urls import path, include
from . import views




urlpatterns = [
    path('profile/<int:user_id>/', views.profile_view, name="profile_view"),
    path('', views.index, name="index"),
    path('<post_id>', views.post_detail, name="post_detail"),
    path('create-post/', views.create_post, name="create_post"),
    path('like/', views.like_post, name="like-post"),
    path('post/<int:post_id>/add-comment/', views.add_comment, name='add_comment'),
]