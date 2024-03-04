from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'games', views.ListCreateGames)
urlpatterns = [
    path('games/join/<int:pk>/', views.JoinInGames.as_view()),
    path('games/user-games/', views.ListUserGames.as_view()),
    path('', include(router.urls)),
]
