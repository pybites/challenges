import json
import pytest

import app

items = [
    {
        'id': 1,
        'name': 'laptop',
        'value': 1000
    },
    {
        'id': 2,
        'name': 'chair',
        'value': 300,
    },
    {
        'id': 3,
        'name': 'book',
        'value': 20,
    },
]


def test_get_items():
    client = app.app.test_client()
    response = client.get('/api/v1.0/items')
    assert json.loads(response.data)['items'] == items


@pytest.mark.parametrize('item_id', [(1), (2), (3)])
def test_get_one_item(item_id):
    client = app.app.test_client()
    
    response = client.get(f'/api/v1.0/items/{item_id}')
    assert json.loads(response.data)['items'][0] == items[item_id-1]
    
    response = client.get('/api/v1.0/items/4')
    assert response.status_code == 404


@pytest.mark.parametrize('name, value, id', [
    ('cd', 10, 4), 
    ('mp3 player', 300, 5),
    ('desk', 100, 6)
])
def test_post_item(name, value, id):
    client = app.app.test_client()

    item = {'name': name, 'value': value}
    response = client.post('/api/v1.0/items', data=json.dumps(item), content_type='application/json')
    assert response.status_code == 201
    item['id'] = id
    assert json.loads(response.data)['item'] == item


@pytest.mark.parametrize('new_value, id', [
    (3000, 1), 
    (200, 2)
])
def test_update_item(new_value, id):
    client = app.app.test_client()

    response = client.get(f'/api/v1.0/items/{id}')
    item = json.loads(response.data)['items'][0]
    item['value'] = new_value
    response = client.put(f'/api/v1.0/items/{id}', data=json.dumps(item), content_type='application/json')
    assert json.loads(response.data)['item'] == item


def test_delete_item():
    client = app.app.test_client()

    response = client.delete('/api/v1.0/items/1')
    assert response.status_code == 204
    response = client.get('/api/v1.0/items/1')
    assert response.status_code == 404
