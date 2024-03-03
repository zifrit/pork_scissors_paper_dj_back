from rest_framework import serializers
from .. import models


class GamesSerializers(serializers.ModelSerializer):
    creator = serializers.CharField(source='creator.username')

    def to_representation(self, instance):
        my_representation = super(GamesSerializers, self).to_representation(instance)
        my_representation['players'] = f'{instance.players.all().count()}/2'
        return my_representation

    class Meta:
        model = models.Games
        fields = ['id', 'creator', 'game_name']
