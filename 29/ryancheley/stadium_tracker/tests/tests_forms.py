from django.test import TestCase
from stadium_tracker.forms import GameDetailsForm
from datetime import datetime
import pytz


class GameDetailsFormTest(TestCase):

    def test_game_getail_form(self):
        data = {
            'home_team': 'LA Dodgers',
            'home_runs': 1,
            'home_hits': 1,
            'home_errors': 1,
            'away_team': 'SF Giants',
            'away_runs': 0,
            'away_hits': 0,
            'away_errors': 0,
            'game_datetime': datetime(year=2017, month=7, day=4, tzinfo=pytz.UTC),
            'game_headline': 'headline',
            'game_body': 'body',
            'game_id': 1,
            'venue_id': 1,
            'user_id': 1
        }
        form = GameDetailsForm(data=data)
        self.assertIn('type="hidden" name="home_team"', form.as_p(),)
        self.assertIn('type="hidden" name="home_runs"', form.as_p(),)
        self.assertIn('type="hidden" name="home_hits"', form.as_p(),)
        self.assertIn('type="hidden" name="home_errors"', form.as_p(),)
        self.assertIn('type="hidden" name="away_team"', form.as_p(),)
        self.assertIn('type="hidden" name="away_runs"', form.as_p(),)
        self.assertIn('type="hidden" name="away_hits"', form.as_p(),)
        self.assertIn('type="hidden" name="away_errors"', form.as_p(),)
        self.assertIn('type="hidden" name="game_datetime"', form.as_p(),)
        self.assertIn('type="hidden" name="game_headline"', form.as_p(),)
        self.assertIn('type="hidden" name="game_body"', form.as_p(),)
        self.assertIn('type="hidden" name="game_id"', form.as_p(),)
        self.assertIn('type="hidden" name="venue_id"', form.as_p(),)
