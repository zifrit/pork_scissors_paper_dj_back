# Generated by Django 5.0.2 on 2024-03-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_user_app', '0004_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='Номер телефона'),
        ),
    ]