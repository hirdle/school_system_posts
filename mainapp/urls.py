from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.posts, name="posts"),
    path('create_post/', views.create_post, name="create_post"),
    path('posts_all/', views.posts_all, name="posts_all"),
    path('post_detail/<int:postid>/', views.post_detail, name="post_detail"),
    path('post_delete/<int:postid>/', views.post_delete, name="post_delete"),
]