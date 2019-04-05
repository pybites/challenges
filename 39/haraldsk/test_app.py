from app import app
import pytest
from flask import json
from flask.testing import FlaskClient


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_get_no_items(client: FlaskClient):
    rv = client.get('/')
    assert b'Not found' in rv.data


def test_get_items(client: FlaskClient):
    rv = client.get('/api/v1.0/items')
    parsed_data = json.loads(rv.data)
    assert parsed_data['items'][0]['id'] == 1


def test_get_item(client: FlaskClient):
    rv = client.get('/api/v1.0/items/1')
    parsed_data = json.loads(rv.data)
    assert parsed_data['items'][0]['id'] == 1
    rv = client.get('/api/v1.0/items/4')
    assert b'Not found' in rv.data


@pytest.mark.parametrize("arg, ret", [
    ({'name': 'PC', 'value': 5000}, b'PC'),
    ({'value': 5000}, b'Bad request'),
    ({'name': 'laptop', 'value': 300}, b'Bad request'),
    ({'name': 'Mackintosh', 'value': 'a string'}, b'Bad request'),
])
def test_create_item(client: FlaskClient, arg, ret):
    rv = client.post('/api/v1.0/items', json=arg)
    assert ret in rv.data


@pytest.mark.parametrize("item, payload, ret", [
    (273, {'name': 'PC',      'value': 5000}, b'Not found'),
    (1,   {'name': 'Updated', 'value': 50}, b'Updated'),
    (2,   {'name': 'Comp',    'value': 'astring'}, b'Bad request'),
])
def test_update_item(client: FlaskClient, item, payload, ret):
    assert ret in client.put('/api/v1.0/items/' + str(item), json=payload).data
    assert b'Bad request' in client.put('/api/v1.0/items/1', data='NotJson').data


def test_delete_item(client: FlaskClient):
    assert b'Not found' in client.delete('/api/v1.0/items/100').data
    assert b'' in client.delete('/api/v1.0/items/1').data
