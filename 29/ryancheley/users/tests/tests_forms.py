from django.test import TestCase, override_settings
from users.models import CustomUser
from users.forms import CustomUserChangeForm


class CustomUserChangeFormTest(TestCase):

    def test_valid_data(self):
        form = CustomUserChangeForm({
            'username': "TurangaLeela",
            'email': "leela@example.com",
            'twitter_user': "test",
            'instagram_user': "test_gram",
            'favorite_team': 119,
            'password': 'abc123++'

        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, "TurangaLeela")
        self.assertEqual(user.email, "leela@example.com")
        self.assertEqual(user.twitter_user, "test")
        self.assertEqual(user.instagram_user, "test_gram")
        self.assertEqual(user.favorite_team, 119)

    def test_blank_data(self):
        form = CustomUserChangeForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['This field is required.'],
            'favorite_team': ['This field is required.'],
        })
