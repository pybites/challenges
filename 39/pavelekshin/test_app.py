import pytest
import json

from app import app

BASE_URL = "http://127.0.0.1:5000/api/v1.0/items"
BAD_ITEM_URL = "{}/5".format(BASE_URL)
GOOD_ITEM_URL = "{}/3".format(BASE_URL)


def setUp():
    backup_items = deepcopy(app.items)
    app = app.test_client()
    assert app.testing == False


def test_get_items():
    with app.test_client() as tc:
        # get items
        response = tc.get(BASE_URL)
        assert response.status_code == 200
        data = json.loads(response.data)
        # items count in response
        assert len(data["items"]) == 3


def test_get_item():
    with app.test_client() as tc:
        # get one non exist item
        response = tc.get(BAD_ITEM_URL)
        assert response.status_code == 404
        # get one exist item
        response = tc.get(GOOD_ITEM_URL)
        data = json.loads(response.data)
        assert response.status_code == 200
        assert len(data["items"]) == 1


def test_not_found():
    with app.test_client() as tc:
        response = tc.get(BAD_ITEM_URL)
        assert response.status_code == 404


def test_bad_request():
    item = {"name": "laptop", "some-value": "1000"}
    # item wrong request body
    with app.test_client() as tc:
        response = tc.post(
            BASE_URL, data=json.dumps(item), content_type="application/json"
        )
        assert response.status_code == 400


def test_create_item():
    with app.test_client() as tc:
        # wrong request body
        item = {"name": "laptop", "some-value": "1000"}
        response = tc.post(
            BASE_URL, data=json.dumps(item), content_type="application/json"
        )
        assert response.status_code == 400
        # item exist
        item = {"name": "laptop", "value": int(1)}
        response = tc.post(
            BASE_URL, data=json.dumps(item), content_type="application/json"
        )
        assert response.status_code == 400
        # item wrong request value type
        item = {"name": "monitor", "value": str(1)}
        response = tc.post(
            BASE_URL, data=json.dumps(item), content_type="application/json"
        )
        assert response.status_code == 400
        # create item
        item = {"name": "printer", "value": 100}
        reponse = tc.post(
            BASE_URL, data=json.dumps(item), content_type="application/json"
        )


def test_update_item():
    item = {"name": "laptop", "some-value": "1000"}
    # item wrong request body
    with app.test_client() as tc:
        response = tc.post(
            BASE_URL, data=json.dumps(item), content_type="application/json"
        )
        assert response.status_code == 400


def test_update_item():
    with app.test_client() as tc:
        # update non exist item
        response = tc.put(BAD_ITEM_URL)
        assert response.status_code == 404
        # empty request body
        response = tc.put(
            GOOD_ITEM_URL, data=json.dumps({}), content_type="application/json"
        )
        assert response.status_code == 400
        # request body contains str instead of int value
        response = tc.put(
            GOOD_ITEM_URL,
            data=json.dumps({"name": "book", "value": str(10)}),
            content_type="application/json",
        )
        assert response.status_code == 400
        # correct request
        response = tc.put(
            GOOD_ITEM_URL,
            data=json.dumps({"name": "book", "value": int(10)}),
            content_type="application/json",
        )
        assert response.status_code == 200


def test_delete_item():
    with app.test_client() as tc:
        # delete non exist item
        response = tc.delete(BAD_ITEM_URL)
        assert response.status_code == 404
        # delete exist item
        response = tc.delete(GOOD_ITEM_URL)
        assert response.status_code == 204


def setDown():
    # reset state
    app.items = backup_items
