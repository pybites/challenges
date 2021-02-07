from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.utils import timezone

from users.models import CustomUser

from stadium_tracker.views import *
from datetime import datetime
import pytz


class TestStadiumGamesViewList(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.password = 'test1234'
        self.test_user = CustomUser.objects.create(
            username='testuser',
            favorite_team=119
        )
        self.test_user.set_password(self.password)
        self.test_user.save()
        self.test_game = GameDetails.objects.create(
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
            create_date=timezone.now(),
            modify_date=timezone.now(),
            user_id=self.test_user.id
        )
        self.test_game.save()

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_StadiumGamesViewList_get_query_set(self):
        response = self.client.get(reverse('stadium_tracker:stadium_game_list', kwargs={'venue_id': 22}))
        self.assertEqual(response.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_game_list(self):
        response = self.client.get(reverse('stadium_tracker:game_list'))
        self.assertEqual(response.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_game_list_not_logged_in(self):
        response = self.client.get(reverse('stadium_tracker:my_game_list'))
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_game_list_logged_in(self):
        self.client.login(username=self.test_user.username, password=self.password)
        response = self.client.get(reverse('stadium_tracker:my_game_list'))
        self.assertEqual(response.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_VenueList_get(self):
        response = self.client.get(reverse('stadium_tracker:venue_list'))
        self.assertEqual(response.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_MyVenues_get_not_logged_in(self):
        response = self.client.get(reverse('stadium_tracker:my_venues'))
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_MyVenues_get_logged_in(self):
        self.client.login(username=self.test_user.username, password=self.password)
        response = self.client.get(reverse('stadium_tracker:my_venues'))
        self.assertEqual(response.status_code, 200)

    def test_GameDetailCreate_get_not_logged_in(self):
        response = self.client.get(reverse('stadium_tracker:gamedetails_create'))
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_GameDetailCreate_get_logged_in(self):
        self.client.login(username=self.test_user.username, password=self.password)
        response = self.client.get(reverse('stadium_tracker:gamedetails_create'))
        self.assertEqual(response.status_code, 200)

    def test_GameDetailDelete_not_logged_in(self):
        id = self.test_game.id
        response = self.client.get(reverse('stadium_tracker:gamesseen_delete', kwargs={'pk': id}))
        self.assertEqual(response.status_code, 302)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_GameDetailDelete_logged_in(self):
        id = self.test_game.id
        self.client.login(username=self.test_user.username, password=self.password)

        response = self.client.get(reverse('stadium_tracker:gamesseen_delete', kwargs={'pk': id}))
        self.assertEqual(response.status_code, 200)
