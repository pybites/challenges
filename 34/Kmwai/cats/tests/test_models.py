from django.test import TestCase

from ..models import Cats


class CatTest(TestCase):
    """test module for Cats model"""

    def setUp(self):
        Cats.objects.create(name='Lion', genus='Panthera', species='P.leo', binomial_name='Panthera Leo')
        Cats.objects.create(name='Jaguar', genus='Panthera', species='P.onca', binomial_name='Panthera Onca')

    def test_cat_genus(self):
        cat_lion = Cats.objects.get(name='Lion')
        cat_jaguar = Cats.objects.get(name='Jaguar')

        self.assertEqual(cat_lion.__str__(), 'Lion belongs to the Panthera genus.')
        self.assertEqual(cat_jaguar.__str__(), 'Jaguar belongs to the Panthera genus.')