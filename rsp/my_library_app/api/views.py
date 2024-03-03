from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from my_user_app import models as my_user_models
from . import serializers
from .. import models


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"


class ListCreateGames(generics.ListCreateAPIView):
    queryset = models.Games.objects.all()
    serializer_class = serializers.GamesSerializers
    pagination_class = CustomPagination
    filterset_fields = [
        'game_name',
    ]

    def create(self, request, *args, **kwargs):
        data = request.data
        creator = my_user_models.CustomUser.objects.get(tg_id=data['id'])
        game = models.Games.objects.create(creator=creator, game_name=data['game_name'])
        game.players.add(creator.id)

        return Response({'status': True,
                         'massage': 'Игра создана'})
