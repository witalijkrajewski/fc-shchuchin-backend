from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player

        fields = (
            'id',
            'get_player_full_name',
            'get_player_age',
            'get_player_team',
            'position',
            'matches',
            'goals',
            'assists',
            'get_player_image',
            'get_player_thumbnail',
            'get_absolute_url',
        )


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)

    class Meta:
        model = Team

        fields = (
            'id',
            'name',
            'location',
            'description',
            'players',
            'get_team_image',
            'get_team_thumbnail',
            'get_absolute_url',
        )
