from copy import deepcopy

import app

assert len(app.items) == 3


class TestDb():

    def __enter__(self):
        self.backup = deepcopy(app.items)
        return app.items

    def __exit__(self, *args):
        app.items = self.backup


def test_post():
    with TestDb() as db:
        newitem = {"name": "screen", "value": 200}
        db.append(newitem)
        assert len(db) == 4
    assert len(app.items) == 3


def test_delete():
    with TestDb() as db:
        db.pop()
        assert len(db) == 2
    assert len(app.items) == 3
