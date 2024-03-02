from django.contrib import admin
from . import models


@admin.register(models.Games)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ['id', 'game_name']
    list_display_links = ['id', 'game_name']
