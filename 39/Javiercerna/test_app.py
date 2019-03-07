import json
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


def test_get_one_item():
    client = app.app.test_client()
    
    response = client.get('/api/v1.0/items/1')
    assert json.loads(response.data)['items'][0] == items[0]
    
    response = client.get('/api/v1.0/items/2')
    assert json.loads(response.data)['items'][0] == items[1]

    response = client.get('/api/v1.0/items/3')
    assert json.loads(response.data)['items'][0] == items[2]

    response = client.get('/api/v1.0/items/4')
    assert response.status_code == 404


def test_post_item():
    client = app.app.test_client()

    item = {'name': 'cd', 'value': 10}
    response = client.post('/api/v1.0/items', data=json.dumps(item), content_type='application/json')
    assert response.status_code == 201
    item['id'] = 4
    assert json.loads(response.data)['item'] == item

    item = {'name': 'mp3 player', 'value': 300}
    response = client.post('/api/v1.0/items', data=json.dumps(item), content_type='application/json')
    assert response.status_code == 201
    item['id'] = 5
    assert json.loads(response.data)['item'] == item

    item = {'name': 'desk', 'value': 100}
    response = client.post('/api/v1.0/items', data=json.dumps(item), content_type='application/json')
    assert response.status_code == 201
    item['id'] = 6
    assert json.loads(response.data)['item'] == item


def test_update_item():
    client = app.app.test_client()

    response = client.get('/api/v1.0/items/1')
    item = json.loads(response.data)['items'][0]
    item['value'] = 3000
    response = client.put('/api/v1.0/items/1', data=json.dumps(item), content_type='application/json')
    assert json.loads(response.data)['item'] == item

    response = client.get('/api/v1.0/items/2')
    item = json.loads(response.data)['items'][0]
    item['value'] = 200
    response = client.put('/api/v1.0/items/2', data=json.dumps(item), content_type='application/json')
    assert json.loads(response.data)['item'] == item


def test_delete_item():
    client = app.app.test_client()

    response = client.delete('/api/v1.0/items/1')
    assert response.status_code == 204
    response = client.get('/api/v1.0/items/1')
    assert response.status_code == 404
