from app import app, get_items, _record_exists, _get_item, create_item
import pytest
import requests
from flask import json

url = 'http://127.0.0.1:5000'

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_get_item():
    assert _get_item(1) == [{'id': 1, 'name': 'laptop', 'value': 1000}]
    assert _get_item(2) == [{'id': 2, 'name': 'chair', 'value': 300}]
    assert _get_item(3) == [{'id': 3, 'name': 'book', 'value': 20}]
    assert _get_item(4) == []
    assert _get_item('a') == []

def test_record_exists():
    assert _record_exists('laptop') == [{'id': 1, 'name': 'laptop', 'value': 1000}]
    assert _record_exists('chair') == [{'id': 2, 'name': 'chair', 'value': 300}]
    assert _record_exists('book') == [{'id': 3, 'name': 'book', 'value': 20}]
    assert _record_exists(4) == []
    assert _record_exists('a') == []

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_get_items():
    res = requests.get(url + '/api/v1.0/items')
    assert res.status_code == 200

    data = res.json()
    assert data['items'][0]['id'] == 1
    assert data['items'][1]['id'] == 2
    assert data['items'][2]['id'] == 3

def test_get_item():
    # Verify a successful connection
    res = requests.get(url + '/api/v1.0/items/1')
    assert res.status_code == 200

    # Verify correct data
    data = res.json()
    assert data['items'][0]['id'] == 1

    # Check for a item outside the list
    res = requests.get(url + '/api/v1.0/items/42')
    assert res.status_code == 404


def test_create_item(client):
    # check for 400 return if id is missing
    res = requests.post(url + '/api/v1.0/items', data=json.dumps({'name': 'lamp', 'value': 5000}))
    assert res.status_code == 400

    # check for 400 return if value is missing
    res = requests.post(url + '/api/v1.0/items', data=json.dumps({'id': '4', 'value': 5000}))
    assert res.status_code == 400

    # return 400 if data is not json
    input = {'name': 'lamp', 'value': 250}
    res = client.post(url + '/api/v1.0/items', data=input, content_type='application/json')
    assert res.status_code == 400

    # check for 400 if name already exists
    res = requests.post(url + '/api/v1.0/items', data=json.dumps({'id': '4', 'name ': 'laptop', 'value': 5000}))
    assert res.status_code == 400

    # check for 400 if value is not an int
    res = requests.post(url + '/api/v1.0/items', data=json.dumps({'id': '4', 'name ': 'laptop', 'value': 'Forty-two'}))
    assert res.status_code == 400

    # check for the correct addition of an item
    input = {'name': 'lamp', 'value': 250}
    res = client.post(url + '/api/v1.0/items', data=json.dumps(input), content_type='application/json')

    assert res.status_code == 201

    data = json.loads(res.get_data())
    assert data['item']['name'] == 'lamp'

def test_update_item(client):
    # return 404 if id is not given
    input = {'id': '', 'name': 'lamp', 'value': 5000}
    res = client.put(url + '/api/v1.0/items/', data=json.dumps(input), content_type='application/json')
    assert res.status_code == 404

    # return 400 if data is not json
    input = {'id': '', 'name': 'lamp', 'value': 5000}
    res = client.put(url + '/api/v1.0/items/', data=input, content_type='application/json')
    assert res.status_code == 404

    # check for 400 if value is not an int
    res = client.put(url + '/api/v1.0/items/1', data=json.dumps({'id': '1', 'name ': 'laptop', 'value': 'Forty-two'}))
    assert res.status_code == 400

    # check for the correct update of an item
    input = {'id': '1', 'name': 'lamp', 'value': 250}
    res = client.put(url + '/api/v1.0/items/1', data=json.dumps(input), content_type='application/json')

    assert res.status_code == 200

    data = json.loads(res.get_data())
    assert data['item']['name'] == 'lamp'

def test_delete_item(client):
    # return 404 if id is not given
    input = {'id': '', 'name': 'lamp', 'value': 5000}
    res = client.delete(url + '/api/v1.0/items/', data=json.dumps(input), content_type='application/json')
    assert res.status_code == 404

    # check for the correct deletion of an item
    res = client.delete(url + '/api/v1.0/items/1')
    assert res.status_code == 204

    res = client.get(url + '/api/v1.0/items/1')
    assert res.status_code == 404
