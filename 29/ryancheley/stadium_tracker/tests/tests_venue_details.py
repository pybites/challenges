from django.test import TestCase
from stadium_tracker.venue_details import *


class TestVenueDetails(TestCase):

    def test_get_venue_details(self):
        x = get_venue_details(22)
        self.assertEqual(x, 'Dodger Stadium')

    def test_get_venue_list(self):
        x = get_venue_list(1, 202)
        self.assertEqual(x[0].get('team_name'), 'Detroit Tigers')
        self.assertEqual(x[0].get('venue_name'), 'Comerica Park')
        self.assertEqual(x[0].get('venue_id'), 2394)
        self.assertEqual(x[0].get('league_id'), 103)
        self.assertEqual(x[0].get('division_id'), 202)
        self.assertEqual(x[0].get('user_visited'), None)
        self.assertEqual(x[0].get('visit_count'), 0)
