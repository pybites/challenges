from django.test import TestCase

class SimpleTests(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_blog_page(self):
        response = self.client.get('/Blog/')
        self.assertEqual(response.status_code, 200)