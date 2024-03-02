from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('games/', views.ListCreateGames.as_view()),
]
