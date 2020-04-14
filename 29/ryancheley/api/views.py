from rest_framework import generics
from .serializers import UsersSerializer, GameDetailsSerializer
from .permissions import IsOwnerOrReadOnly

from stadium_tracker.models import GameDetails


class GameDetailsList(generics.ListAPIView):
    """
    get:
    Return a list of all Games Seen in the database
    post:
    Create a Game Seen for a named user
    """
    queryset = GameDetails.objects.all()
    serializer_class = GameDetailsSerializer


class GameDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return an individual Game Seen for a Named User

    delete:
    Remove a Game Seen for a user

    put:
    Update a Game Seen for a named user

    """

    permission_classes = (IsOwnerOrReadOnly, )
    queryset = GameDetails.objects.all()
    serializer_class = GameDetailsSerializer

