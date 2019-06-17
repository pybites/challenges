import pytest
import json
from app import app


@pytest.fixture
def client(request):
    client = app.test_client()
    return client


def test_get_items(client):
    res = client.get('/api/v1.0/items')
    assert res.status_code == 200
    assert len(json.loads(res.data)['items']) == 3

@pytest.mark.parametrize('id, expected', [ 
    (1, [{'id': 1, 'name': 'laptop', 'value': 1000}]),
    (2, [{'id': 2, 'name': 'chair', 'value': 300}]),
    (3, [{'id': 3, 'name': 'book', 'value': 20}]),
    ])
def test_get_item(client, id, expected):
    res = client.get('/api/v1.0/items/' + str(id))
    assert res.status_code == 200
    assert json.loads(res.data)['items'] == expected


@pytest.mark.parametrize('id, values, expected', [ 
    (1, {'name': 'laptop', 'value': 2000}, {'item': {'id': 1, 'name': 'laptop', 'value': 2000}}),
    (2, {'name': 'desk', 'value': 300}, {'item': {'id': 2, 'name': 'desk', 'value': 300}} ),
    (3, {'name': 'book', 'value': '30'}, {'error': 'Bad request'}),
    (120, {'name': 'bike', 'value': 2000}, {'error': 'Not found'}),
])
def test_update_item(client, id, values, expected):
    res = client.put('/api/v1.0/items/' + str(id), json=values)
    assert json.loads(res.data) == expected

def test_update_item_not_json(client):
    res = client.put('/api/v1.0/items/1', data='NotJson')
    assert res.status_code == 400


@pytest.mark.parametrize('values, expected', [ 
    ({'name': 'iphone', 'value': 1500}, b'iphone'),
    ({'name': 'monitor', 'value': 1300}, b'monitor' ),
    ({'name': 'robot', 'value': 800}, b'robot'),
])
def test_create_item(client, values, expected):
    res = client.post('/api/v1.0/items', json=values)
    assert res.status_code == 201
    assert expected in res.data


@pytest.mark.parametrize('id, expected', [ 
    (2, b''),
    (3, b''),
    (300, b'{"error":"Not found"}\n')
])
def test_delete_item(client, id, expected):
    res = client.delete('/api/v1.0/items/' + str(id))
    assert res.data == expected


@pytest.mark.parametrize('id, expected', [ 
    (100, {'error': 'Not found'}),
    (120, {'error': 'Not found'}),
    ])
def test_not_found(client, id, expected):
    res = client.get('/api/v1.0/items/' + str(id))
    assert res.status_code == 404
    assert json.loads(res.data) == expected


@pytest.mark.parametrize('values, expected', [ 
    ({'name': 'laptop', 'value': 2000}, b'Bad request'),
    ({'name': 'ball', 'value': '20'}, b'Bad request'),
    ({'name': 'toy'}, b'Bad request')
])
def test_bad_request(client, values, expected):
    res = client.post('/api/v1.0/items', json=values)
    assert res.status_code == 400
    assert expected in res.data