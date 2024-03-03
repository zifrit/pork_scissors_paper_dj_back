from django.db import models

from context_app.models import DCU


class Games(DCU):
    TYPEOFGAME = (
        ('rsp', 'Камень, Ножницы, Бумага'),
    )
    creator = models.ForeignKey(to='my_user_app.CustomUser', verbose_name='Создатель', db_index=True,
                                on_delete=models.CASCADE, related_name="my_games")
    game_name = models.CharField(verbose_name='Название игры', max_length=255)
    type_of_game = models.CharField(verbose_name='Тип игры', max_length=100, choices=TYPEOFGAME, default='rsp')
    players = models.ManyToManyField(to='my_user_app.CustomUser', verbose_name='Игроки')

    class Meta:
        db_table = 'LibraryGames'
        verbose_name = 'СписокИгр'
        verbose_name_plural = 'СписокИгр'

    def __str__(self):
        return f'создал {self.creator.__str__()} игру {self.game_name}, id {self.id}'
