from django.test import TestCase
from users.models import CustomUser
from stadium_tracker.league_details import *

class LeagueDetailsTest(TestCase):

    def test_get_team_division(self):
        x = get_team_division(1, 119)
        self.assertEqual(x, 203)

    def test_get_division_details(self):
        user = CustomUser.objects.create_user(username='ryan', favorite_team=119)
        x = get_division_details(1, user)
        self.assertEqual(x[0].get('division_id'), 202)