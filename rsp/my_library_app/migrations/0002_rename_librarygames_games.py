# Generated by Django 5.0.2 on 2024-03-02 22:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_library_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LibraryGames',
            new_name='Games',
        ),
    ]
