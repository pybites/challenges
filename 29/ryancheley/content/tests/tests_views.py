from django.test import TestCase, override_settings
from content.models import Content
from users.models import CustomUser


def create_user(username, favorite_team):
    return CustomUser.objects.create(username=username, favorite_team=favorite_team)


def create_content(title, content):
    author = create_user('ryan', 119)
    return Content.objects.create(title=title, page_content=content, author=author)


class ContentTemplateViewTests(TestCase):

    def test_page_content(self):
        page = create_content('Test', 'Test Page Content')
        self.assertEqual(page.title, 'Test')
        self.assertEqual(page.page_content, 'Test Page Content')

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_page_exists(self):
        page = create_content('Test', 'Test Page Content')
        response = self.client.get(f'/Pages/{page}')
        self.assertEqual(response.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_page_does_not_exist(self):
        page = create_content('Test', 'Test Page Content')
        response = self.client.get(f'/{page}')
        self.assertEqual(response.status_code, 404)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_home_page_name(self):
        page = create_content('Stadia Tracker', 'Home Page Content')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
