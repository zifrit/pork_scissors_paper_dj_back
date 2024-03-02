from rest_framework import serializers
from .. import models


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['username', 'first_name', 'last_name', 'tg_id']

    def create(self, validated_data):
        user = models.CustomUser.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tg_id=validated_data['tg_id'],
        )
        password = f'Spase_{validated_data["tg_id"]}_&!@#$'
        user.set_password(password)
        user.is_active = True
        user.save()
        return user
