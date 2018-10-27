import json
import unittest
from app import app

class TestApp(unittest.TestCase):

    BASE_URL = 'http://localhost:5000/api/v1.0/items'

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_items(self):
        response = self.app.get(TestApp.BASE_URL)
        assert response.status_code == 200

    def test_get_item(self):
        response = self.app.get('{}/2'.format(TestApp.BASE_URL))
        expected = {'items': [{'id': 2, 'name': 'chair', 'value': 300}]}
        data = json.loads(response.get_data())
        assert expected == data

    def test_get_item_not_founc(self):
        response = self.app.get('{}/10'.format(TestApp.BASE_URL))
        assert response.status_code == 404

    def test_create_item(self):
        item = {'id': 4, 'name': 'monitor', 'value': 500}
        dump = json.dumps(item)
        response = self.app.post(TestApp.BASE_URL, 
                                 data=dump,
                                 content_type='application/json')
        assert response.status_code == 201
        assert item == json.loads(response.get_data())['item']

    def test_create_item_no_value(self):
        item = {'id': 4, 'name': 'monitor'}
        dump = json.dumps(item)
        response = self.app.post(TestApp.BASE_URL, 
                                 data=dump,
                                 content_type='application/json')
        assert response.status_code == 400

    def test_create_item_value_no_int(self):
        item = {'id': 7, 'name': 'mouse', 'value': 'dd'}
        dump = json.dumps(item)
        response = self.app.post(TestApp.BASE_URL, 
                                 data=dump,
                                 content_type='application/json')
        assert response.status_code == 400

    def test_create_item_already_exists(self):
        item = {'id': 5, 'name': 'book', 'value': 20}
        dump = json.dumps(item)
        response = self.app.post(TestApp.BASE_URL, 
                                data=dump,
                                content_type='application/json')
        assert response.status_code == 400

    def test_update_item(self):
        item = {'id': 2, 'name': 'chair', 'value': 531}
        dump = json.dumps(item)
        response = self.app.put('{}/2'.format(TestApp.BASE_URL), 
                                data=dump,
                                content_type='application/json')
        assert response.status_code == 200
        assert item == json.loads(response.get_data())['item']

    def test_delete_item(self):
        response = self.app.delete('{}/1'.format(TestApp.BASE_URL), 
                                   content_type='application/json')
        assert response.status_code == 204

    def test_delete_item_not_found(self):
        response = self.app.delete('{}/1000'.format(TestApp.BASE_URL), 
                                   content_type='application/json')
        assert response.status_code == 404