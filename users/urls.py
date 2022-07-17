from django import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(), name='logout'),
]