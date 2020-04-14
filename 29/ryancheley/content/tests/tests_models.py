from django.test import TestCase
from content.models import Content
from users.models import CustomUser


class ContentTestCase(TestCase):

    def setUp(self) -> None:
        CustomUser.objects.create(
            username='ryan',
            favorite_team=119,
        )

        Content.objects.create(
            title='Home Page',
            page_content='<h2>Home Page</h2><p>This is the home page!</p>',
            author=CustomUser.objects.get(username='ryan'),
        )

    def test_string_representation(self):
        page = Content.objects.get(title='Home Page')
        self.assertEqual(str(page), 'Home Page')

    def test_object_properties(self):
        page = Content.objects.get(title='Home Page')
        self.assertEqual(page.title, 'Home Page')
        self.assertEqual(page.page_content, '<h2>Home Page</h2><p>This is the home page!</p>')
        self.assertEqual(page.author.username, 'ryan')
        self.assertTrue(isinstance(page, Content))
