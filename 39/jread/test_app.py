import app
import json
import pytest

CLIENT = app.app.test_client()


@pytest.mark.parametrize('item_id', [1, 2, 3])
def test_get_item(item_id: int):
    response = CLIENT.get(f'/api/v1.0/items/{item_id}')
    assert json.loads(response.data)['items'][0] == app.items[item_id - 1]


def test_get_item_not_found():
    response = CLIENT.get('/api/v1.0/items/100')
    assert response.status_code == 404


def test_get_items():
    response = CLIENT.get('/api/v1.0/items')
    assert json.loads(response.data)['items'] == app.items


@pytest.mark.parametrize('name, value', [
    ('monitor', 500),
    ('desk', 1000),
    ('keyboard', 100)
])
def test_create_item(name: str, value: int):
    item = {'name': name, 'value': value}
    response = CLIENT.post('/api/v1.0/items', data=json.dumps(item), content_type='application/json')
    assert response.status_code == 201
    assert json.loads(response.data)['item'] == app.items[-1]


@pytest.mark.parametrize('value, item_id', [
    (500, 1),
    (1000, 2)
])
def test_update_item(value: int, item_id: int):
    item = json.loads(CLIENT.get(f'/api/v1.0/items/{item_id}').data)['items'][0]
    item['value'] = value
    response = CLIENT.put(f'/api/v1.0/items/{item_id}', data=json.dumps(item), content_type='application/json')
    assert json.loads(response.data)['item'] == item


@pytest.mark.parametrize('item_id, status_code', [
    (1, 204),
    (1, 404)
])
def test_delete_item(item_id: int, status_code: int):
    response = CLIENT.delete(f'/api/v1.0/items/{item_id}')
    assert response.status_code == status_code