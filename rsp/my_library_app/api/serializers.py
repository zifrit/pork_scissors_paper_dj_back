from rest_framework import serializers
from .. import models


class GamesSerializers(serializers.ModelSerializer):
    creator = serializers.CharField(source='creator.username')

    def to_representation(self, instance):
        my_representation = super(GamesSerializers, self).to_representation(instance)
        my_representation['players'] = instance.players.all().count()
        return my_representation

    class Meta:
        model = models.Games
        fields = ['creator', 'game_name']
