from rest_framework import serializers
from api.models import Challenge

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('id', 'url','title',)
