from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from context_app.models import DCU


class CustomUserManager(UserManager):

    def all(self):
        return self.filter(is_superuser=False)


class CustomUser(AbstractUser, DCU):
    """Расширенный базовый пользователь"""
    phone = models.CharField(max_length=12, unique=True, verbose_name='Номер телефона')
    tg_id = models.CharField(max_length=20, unique=True, verbose_name='ID Телеграмма', db_index=True)
    objects = CustomUserManager()

    class Meta:
        db_table = 'CustomUser'
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.username
