from copy import deepcopy

import app


class CopyDb():

    def __enter__(self):
        self.backup = deepcopy(app.items)
        return app.items

    def __exit__(self, *args):
        app.items = self.backup


def test_post():
    with CopyDb() as db:
        newitem = {"name": "screen", "value": 200}
        db.append(newitem)
        assert len(db) == 4
    assert len(app.items) == 3


def test_delete():
    with CopyDb() as db:
        db.pop()
        assert len(db) == 2
    assert len(app.items) == 3
