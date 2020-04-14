from rest_framework import serializers

from stadium_tracker.models import GameDetails
from users.models import CustomUser


class GameDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameDetails
        fields = (
            'home_team',
            'home_runs',
            'home_hits',
            'home_errors',
            'away_team',
            'away_runs',
            'away_hits',
            'away_errors',
            'game_datetime',
            'game_headline',
            'game_body',
            'game_id',
            'venue_id',
            'user_id',
        )


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')