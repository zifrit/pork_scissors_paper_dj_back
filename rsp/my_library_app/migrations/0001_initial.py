# Generated by Django 5.0.2 on 2024-03-02 12:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete', models.BooleanField(default=False, help_text='Состояние удалена ли данная запись', verbose_name='Удален')),
                ('date_delete', models.DateTimeField(blank=True, null=True, verbose_name='Время удаления')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('game_name', models.CharField(max_length=255, verbose_name='Пачка')),
                ('type_of_game', models.CharField(choices=[('rsp', 'Камень, Ножницы, Бумага')], default='rsp', max_length=100, verbose_name='Тип игры')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_games', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Игроки')),
            ],
            options={
                'verbose_name': 'СписокИгр',
                'verbose_name_plural': 'СписокИгр',
                'db_table': 'LibraryGames',
            },
        ),
    ]
