from django.shortcuts import render
from api.models import Challenge
from rest_framework import generics
from api.serializers import ChallengeSerializer

# Create your views here.

class ChallengeList(generics.ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class ChallengeDetail(generics.RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer