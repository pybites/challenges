from django.test import TestCase
from stadium_tracker.models import GameDetails
from users.models import CustomUser
from datetime import datetime
import pytz


class GameDetailsTest(TestCase):

    def setUp(self) -> None:
        CustomUser.objects.create(
            username='ryan',
            favorite_team=119
        )

        GameDetails.objects.create(
            home_team='LA Dodgers',
            home_runs=1,
            home_hits=1,
            home_errors=1,
            away_team='SF Giants',
            away_runs=0,
            away_hits=0,
            away_errors=0,
            game_datetime=datetime(year=2019, month=7, day=4, tzinfo=pytz.UTC),
            game_headline='headline',
            game_body='body',
            game_id=1,
            venue_id=1,
            user_id=1
        )

    def test_string_representation(self):
        game = GameDetails.objects.get(game_id=1)
        self.assertEqual(str(game),  'LA Dodgers vs SF Giants (07/04/2019)')

    def test_get_venue_count(self):
        game_count = GameDetails.get_venue_count(self)
        self.assertEqual(game_count[0].get('total'), 1)
        self.assertEqual(game_count[0].get('venue_id'), 1)

    def test_game_user_combination_is_unique(self):
        g = GameDetails.objects.get(game_id=1)
        unique_together = g._meta.unique_together
        self.assertEquals(unique_together[0], ('user', 'game_id'))

    def test_game_details_properties(self):
        g = GameDetails.objects.get(game_id=1)
        self.assertEqual(g.home_team, 'LA Dodgers')
