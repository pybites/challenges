from contextlib import contextmanager
from copy import deepcopy

import app

assert len(app.items) == 3


@contextmanager
def testdb():
    backup = deepcopy(app.items)
    yield app.items
    app.items = backup


def test_post():
    with testdb() as db:
        newitem = {"name": "screen", "value": 200}
        db.append(newitem)
        assert len(db) == 4
    assert len(app.items) == 3


def test_delete():
    with testdb() as db:
        db.pop()
        assert len(db) == 2
    assert len(app.items) == 3
