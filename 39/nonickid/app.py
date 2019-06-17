from flask import Flask, jsonify, abort, make_response, request

NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'

app = Flask(__name__)

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


def _get_item(id):
    return [item for item in items if item['id'] == id]


def _record_exists(name):
    return [item for item in items if item["name"] == name]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQUEST}), 400)


@app.route('/api/v1.0/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})


@app.route('/api/v1.0/items/<int:id>', methods=['GET'])
def get_item(id):
    item = _get_item(id)
    if not item:
        abort(404)
    return jsonify({'items': item})


@app.route('/api/v1.0/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json or 'value' not in request.json:
        abort(400)
    item_id = items[-1].get("id") + 1
    name = request.json.get('name')
    if _record_exists(name):
        abort(400)
    value = request.json.get('value')
    if type(value) is not int:
        abort(400)
    item = {"id": item_id, "name": name,
            "value": value}
    items.append(item)
    return jsonify({'item': item}), 201


@app.route('/api/v1.0/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = _get_item(id)
    if len(item) == 0:
        abort(404)
    if not request.json:
        abort(400)
    name = request.json.get('name', item[0]['name'])
    value = request.json.get('value', item[0]['value'])
    if type(value) is not int:
        abort(400)
    item[0]['name'] = name
    item[0]['value'] = value
    return jsonify({'item': item[0]}), 200


@app.route('/api/v1.0/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = _get_item(id)
    if len(item) == 0:
        abort(404)
    items.remove(item[0])
    return jsonify({}), 204


if __name__ == '__main__':
    app.run(debug=True)
