from django.db import models


class DCU(models.Model):
    delete = models.BooleanField(default=False, verbose_name='Удален', help_text='Состояние удалена ли данная запись')
    date_delete = models.DateTimeField(verbose_name='Время удаления', blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        abstract = True
