from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('games/', views.ListCreateGames.as_view()),
    path('games/join/<int:pk>/', views.JoinInGames.as_view()),
    path('games/user-games/', views.ListUserGames.as_view()),
]
