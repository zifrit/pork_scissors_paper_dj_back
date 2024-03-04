import datetime

from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics, status, mixins
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from telebot import TeleBot

from my_user_app import models as my_user_models
from . import serializers
from .. import models

bot = TeleBot('5499674135:AAH5OyMw3daMSptBKnHnF_wXj9ho2sJpsz4')


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"


class ListCreateGames(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = models.Games.objects.all()
    serializer_class = serializers.GamesSerializers
    pagination_class = CustomPagination
    filterset_fields = [
        'game_name',
    ]

    @action(methods=['get'], detail=True, url_path='player')
    def player(self, request, pk):
        games = models.Games.objects.get(id=pk)
        player = {user.tg_id: user.username for user in games.players.all()}
        if games.players.all().count() == 2:
            return Response({'status': True, 'players': player, 'games_name': games.game_name},
                            status=status.HTTP_200_OK)
        return Response({'status': False, 'players': player, 'games_name': games.game_name,
                         'message': 'В комнате не достаточно игроков'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        data = request.data
        creator = my_user_models.CustomUser.objects.get(tg_id=data['id'])
        game = models.Games.objects.create(creator=creator, game_name=data['game_name'])
        game.players.add(creator.id)

        return Response({'status': True,
                         'message': 'Игра создана'})

    def destroy(self, request, *args, **kwargs):
        game = self.get_object()
        game.delete = True
        game.date_delete = datetime.datetime.now()
        game.save()
        return Response({'status': True,
                         'message': 'Игра удалена'}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='delete-players')
    def delete_players(self, request, pk):
        games = models.Games.objects.get(id=pk)
        games.players.clear()
        games.players.add(games.creator.id)
        games.save()
        return Response({'status': True,
                         'message': 'Игроки удалены'}, status=status.HTTP_200_OK)


class JoinInGames(generics.GenericAPIView):

    def post(self, request, pk):
        data = request.data
        games = models.Games.objects.get(id=pk)
        count_players = games.players.all().count()
        if games.creator.tg_id == str(data['player']):
            return Response({'status': False,
                             'message': 'Вы не можете присоединится к совой же игре'},
                            status=status.HTTP_400_BAD_REQUEST)
        elif count_players == 2:
            return Response({'status': False,
                             'message': 'комната уже заполнены'},
                            status=status.HTTP_400_BAD_REQUEST)
        elif count_players < 2:
            user = my_user_models.CustomUser.objects.get(tg_id=data['player'])
            games.players.add(user.id)
            games.save()
            bot.send_message(chat_id=games.creator.tg_id,
                             text=f'К комнате присоединился человек игру можно начать /start_rsp_{games.id}')
            return Response({'status': True,
                             'message': 'Вы присоединились к игре'},
                            status=status.HTTP_200_OK)
        return Response({1: 1})


class ListUserGames(generics.ListAPIView):
    queryset = models.Games.objects.all()
    serializer_class = serializers.UserGamesSerializers
    pagination_class = CustomPagination

    def get_queryset(self):
        data = self.request.data
        return models.Games.objects.filter(creator__tg_id=data['id'], delete=False)
