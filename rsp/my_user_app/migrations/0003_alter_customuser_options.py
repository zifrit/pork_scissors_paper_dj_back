# Generated by Django 5.0.2 on 2024-03-02 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_user_app', '0002_customuser_date_create_customuser_date_delete_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
