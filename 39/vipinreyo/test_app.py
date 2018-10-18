import json
import pytest

import app

BASE_URL = 'http://127.0.0.1:5000/api/v1.0/items'


@pytest.fixture(scope='session')
def get_test_client():
    test_client = app.app.test_client()
    test_client.testing = True

    return test_client


def test_get_items(get_test_client):
    """Test to check the API get_items"""

    test_client = get_test_client
    response = test_client.get(BASE_URL)
    data = json.loads(response.get_data())

    assert response.status_code == 200
    assert len(data['items']) == 3


def test_get_item(get_test_client):
    """Test to verify the API get_item"""

    test_client = get_test_client
    url = BASE_URL + '/1'
    response = test_client.get(url)
    data = json.loads(response.get_data())

    assert response.status_code == 200
    assert data['items'][0]['name'] == 'laptop'


def test_get_no_item(get_test_client):
    """Test to verify the API get_item if no item is found"""

    test_client = get_test_client
    url = BASE_URL + '/145'
    response = test_client.get(url)

    assert response.status_code == 404


def test_create_item(get_test_client):
    """Test to verify the create_item API"""

    test_client = get_test_client

    # Check if the API handles the request as designed if item details are missing ('value' field missing)
    item = {'name': 'dummy'}
    response = test_client.post(BASE_URL, data=json.dumps(item), content_type='application/json')
    assert response.status_code == 400

    # Check if the API handles the request as designed if item details are missing ('name field missing)
    item = {'value': 'dummy'}
    response = test_client.post(BASE_URL, data=json.dumps(item), content_type='application/json')
    assert response.status_code == 400

    # Check the behaviour if item is already present
    item = {'name': 'laptop', 'value': 200}
    response = test_client.post(BASE_URL, data=json.dumps(item), content_type='application/json')
    assert response.status_code == 400

    # Check th behaviour if the value is not an integer
    item = {'name': 'dummy', 'value': 'ABCD'}
    response = test_client.post(BASE_URL, data=json.dumps(item), content_type='applicaiton/json')
    assert response.status_code == 400

    # Check if a valid item is added
    item = {'name': 'keyboard', 'value': 250}
    response = test_client.post(BASE_URL, data=json.dumps(item), content_type='application/json')
    assert response.status_code == 201

    data = json.loads(response.get_data())
    assert data['item']['name'] == 'keyboard'


def test_update_item(get_test_client):
    """Test the update_item API"""

    test_client = get_test_client

    # Check the behaviour if a non-existing item is passed to API
    item = {'id': 145, 'name': 'mouse', 'value': 100}
    url = BASE_URL + '/145'
    response = test_client.put(url, data=json.dumps(item), content_type='application/json')
    assert response.status_code == 404

    # Check the behaviour if the data or payload is not in json format
    item = {'id': 1, 'name': 'monitor', 'value': 300}
    url = BASE_URL + '/1'
    response = test_client.put(url, data=item, content_type='application/json')
    assert response.status_code == 400

    # Check the behviour if the value is not an integer
    item = {'id': 1, 'name': 'monitor', 'value': 'ABCD'}
    response = test_client.put(url, data=item, content_type='application/json')
    assert response.status_code == 400

    # Check if update is successful
    item = {'id': 1, 'name': 'monitor', 'value': 400}
    response = test_client.put(url, data=json.dumps(item), content_type='application/json')
    data = json.loads(response.get_data())
    assert data['item']['name'] == 'monitor'
    assert data['item']['value'] == 400


def test_delete_item(get_test_client):
    """Test the delete_item API"""

    test_client = get_test_client

    # Check the behaviour if a non existing item is given
    url = BASE_URL + '/145'
    response = test_client.delete(url)
    assert response.status_code == 404

    # Check if the item is deleted correctly
    url = BASE_URL + '/1'
    response = test_client.delete(url)
    assert response.status_code == 204


