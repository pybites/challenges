import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Cats
from ..serializers import CatSerializer


# initialise client app
client = Client()


class GetAllCatsTest(TestCase):
    """test module for GET all puppies"""
    def setUp(self):
        Cats.objects.create(name='Lion', genus='Panthera', species='P.leo', binomial_name='Panthera Leo')
        Cats.objects.create(name='Jaguar', genus='Panthera', species='P. onca', binomial_name='Panthera Onca')
        Cats.objects.create(name='Lion', genus='Panthera', species='P.leo', binomial_name='Panthera Leo')
        Cats.objects.create(name='Jaguar', genus='Panthera', species='P. onca', binomial_name='Panthera Onca')

    def test_get_all_cats(self):
        # get API response
        response = client.get(reverse('get_post_cats'))

        # get data from db
        cats = Cats.objects.all()
        serializer = CatSerializer(cats, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleCatTest(TestCase):
    """test module for GET single cat"""

    def setUp(self):
        self.lion = Cats.objects.create(name='Lion', genus='Panthera', species='P.leo',
                                        binomial_name='Panthera Leo')
        self.jaguar = Cats.objects.create(name='Jaguar', genus='Panthera', species='P.onca',
                                          binomial_name='Panthera Onca')
        self.cheetah = Cats.objects.create(name='Cheetah', genus='Acinonyx', species='A.jubatus',
                                           binomial_name='Acinonyx jubatus')
        self.leopard = Cats.objects.create(name='Leopard', genus='Panthera', species='P.pardus',
                                           binomial_name='Panthera pardus')

    def test_get_valid_cat(self):
        response = client.get(reverse('get_delete_update_cat', kwargs={'pk': self.lion.pk}))
        cat = Cats.objects.get(pk=self.lion.pk)
        serializer = CatSerializer(cat)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_cat(self):
        response = client.get(reverse('get_delete_update_cat', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewCatTest(TestCase):
    """test module for inserting a new cat"""

    def setUp(self):
        self.valid_load = {
            'name': 'Cheetah',
            'genus': 'Acinonyx',
            'species': 'A.jubatus',
            'binomial_name': 'Panthera jubatus'
        }

        self.invalid_load = {
            'name': '',
            'genus': 'Acinonyx',
            'species': 'A.jubatus',
            'binomial_name': 'Panthera jubatus'
        }

    def test_create_valid_cat(self):
        response = client.post(reverse('get_post_cats'),
                               data=json.dumps(self.valid_load),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_cat(self):
        response = client.post(reverse('get_post_cats'),
                               data=json.dumps(self.invalid_load),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleCatTest(TestCase):
    """test module for updating a cat"""

    def setUp(self):
        self.lion = Cats.objects.create(name='Lion', genus='Panthera', species='P.leo', binomial_name='Panthera Leo')
        self.jaguar = Cats.objects.create(name='Jaguar', genus='Panthera', species='P.onca',
                                          binomial_name='Panthera Onca')

        self.valid_load = {
            'name': 'Cheetah',
            'genus': 'Acinonyx',
            'species': 'A.jubatus',
            'binomial_name': 'Panthera jubatus'
        }

        self.invalid_load = {
            'name': '',
            'genus': 'Acinonyx',
            'species': 'A.jubatus',
            'binomial_name': 'Panthera jubatus'
        }

    def test_valid_load(self):
        response = client.put(reverse('get_delete_update_cat', kwargs={'pk': self.lion.pk}),
                              data=json.dumps(self.valid_load), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_load(self):
        response = client.put(reverse('get_delete_update_cat', kwargs={'pk': self.lion.pk}),
                              data=json.dumps(self.invalid_load), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleCatTest(TestCase):
    """test module for deleting existing single cat"""

    def setUp(self):
        self.lion = Cats.objects.create(name='Lion', genus='Panthera', species='P.leo', binomial_name='Panthera Leo')
        self.jaguar = Cats.objects.create(name='Jaguar', genus='Panthera', species='P.onca',
                                          binomial_name='Panthera Onca')

    def test__valid_delete_cat(self):
        response = client.delete(reverse('get_delete_update_cat', kwargs={'pk': self.lion.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_cat(self):
        response = client.delete(reverse('get_delete_update_cat', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)