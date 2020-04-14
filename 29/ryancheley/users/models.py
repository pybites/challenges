from django.contrib.auth.models import AbstractUser
from django.db import models
from stadium_tracker.game_details import get_teams


class CustomUser(AbstractUser):
    team_choices = []
    teams = get_teams(1)
    for t in teams:
        team_choices.append((t.get('id'), t.get('name')))

    twitter_user = models.CharField(max_length=15, blank=True, null=True)
    instagram_user = models.CharField(max_length=30, blank=True, null=True)
    favorite_team = models.IntegerField(
        choices=team_choices,

    )

