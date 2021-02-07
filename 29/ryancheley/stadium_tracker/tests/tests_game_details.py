from dateutil.tz import tzlocal
from django.test import TestCase
from stadium_tracker.game_details import *


class GameDetails(TestCase):

    def test_get_game_recap_headline_is_None(self):
        x = get_game_recap(8060, 'headline')
        self.assertIsNone(x)

    def test_get_game_recap_body_is_None(self):
        x = get_game_recap(8060, 'body')
        self.assertIsNone(x)

    def test_get_game_recap_headline_is_not_None(self):
        x = get_game_recap(566063, 'headline')
        self.assertIsNotNone(x)
        self.assertEqual(x, 'Dodgers rally in NY, clinch NLDS advantage')

    def test_get_game_recap_body_is_not_None(self):
        x = get_game_recap(566063, 'body')
        self.assertIsNotNone(x)
        self.assertEqual(len(x), 3881)

    def test_get_default_game(self):
        x = get_default_game(1)
        self.assertIsNotNone(x.get('game_date'))
        self.assertIsNotNone(x.get('home_team'))
        self.assertIsNotNone(x.get('away_team'))

    def test_get_game_object(self):
        x = get_game_object(566063)
        self.assertEqual(x.status_code, 200)

    def test_get_game_date(self):
        x = get_game_date(566063)
        self.assertEqual(x, datetime(2019, 9, 15, 23, 5, tzinfo=tzlocal()))

    def test_get_venue_id(self):
        v = get_venue_id(566063)
        self.assertEqual(v, 3289)

    def test_get_boxscore_home_full(self):
        x = get_boxscore(566063, 'home')
        self.assertEqual(x.get('hits'), 3)
        self.assertEqual(x.get('runs'), 2)
        self.assertEqual(x.get('errors'), 0)
        self.assertEqual(x.get('team'), 'New York Mets')

    def test_get_boxscore_away_full(self):
        x = get_boxscore(566063, 'away')
        self.assertEqual(x.get('hits'), 9)
        self.assertEqual(x.get('runs'), 3)
        self.assertEqual(x.get('errors'), 0)
        self.assertEqual(x.get('team'), 'Los Angeles Dodgers')

    def test_get_boxscore_home_not_full(self):
        x = get_boxscore(8060, 'home')
        self.assertEqual(x.get('hits'), None)
        self.assertEqual(x.get('runs'), 2)
        self.assertEqual(x.get('errors'), None)
        self.assertEqual(x.get('team'), 'San Francisco Giants')

    def test_get_boxscore_away_not_full(self):
        x = get_boxscore(8060, 'away')
        self.assertEqual(x.get('hits'), None)
        self.assertEqual(x.get('runs'), 1)
        self.assertEqual(x.get('errors'), None)
        self.assertEqual(x.get('team'), 'Colorado Rockies')

    def test_get_games_for_date_with_games(self):
        x = get_games_for_date(1, '2019-10-19')
        self.assertLessEqual(len(x), 3)
        self.assertIsNotNone(x)

    def test_get_games_for_date_with__nogames(self):
        x = get_games_for_date(1, '2019-12-19')
        self.assertIsNone(x)

