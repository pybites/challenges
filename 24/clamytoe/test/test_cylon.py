import pytest

from cylon import Cylon, prev


@pytest.fixture
def cylon_models():
    # source: https://en.battlestarwikiclone.org/wiki/Cylon_Models
    models = [
        "U-87 Cyber Combat Unit",
        "Civilian Cylon",
        "Cylon War-Era Centurion",
        "Cython",
        "Djerba Centurion",
        "Modern Centurion",
        "Inorganic Humanoids",
        "Cylon Spacecraft",
        "Cylon Hybrids",
        "Humanoid Cylons",
    ]
    return Cylon(models)


def test_empty_object():
    cy = Cylon()
    assert len(cy) == 0
    assert cy.current() is None
    assert str(cy) == "empty"


def test_cylon_object(cylon_models):
    assert isinstance(cylon_models, Cylon)
    assert repr(cylon_models) == "Cylon(items=10 index=0)"
    assert str(cylon_models) == "U-87 Cyber Combat Unit"


def test_cylon_defaults(cylon_models):
    assert len(cylon_models) == 10
    assert cylon_models._index == 0
    assert cylon_models.current() == "U-87 Cyber Combat Unit"


def test_cylon_methods(cylon_models):
    assert next(cylon_models) == "Civilian Cylon"
    assert cylon_models._index == 1
    assert next(cylon_models) == "Cylon War-Era Centurion"
    assert cylon_models._index == 2
    assert next(cylon_models) == "Cython"
    assert cylon_models._index == 3
    assert prev(cylon_models) == "Cylon War-Era Centurion"
    assert cylon_models._index == 2


def test_cylon_boundaries(cylon_models):
    assert cylon_models.current() == "U-87 Cyber Combat Unit"
    assert cylon_models._index == 0
    assert prev(cylon_models) == "Humanoid Cylons"
    assert cylon_models._index == 9
    assert next(cylon_models) == "U-87 Cyber Combat Unit"
    assert cylon_models._index == 0


def test_cylon_indexing(cylon_models):
    assert cylon_models[0] == "U-87 Cyber Combat Unit"
    assert cylon_models[-1] == "Humanoid Cylons"


def test_cylon_inserting():
    lst = "a b c".split()
    cy = Cylon()
    cy.extend(lst)
    assert len(cy) == 3
    assert cy.current() == "a"
    assert next(cy) == "b"
    cy.insert(1, "e")
    assert len(cy) == 4
    assert cy.items == "a e b c".split()
    cy.insert(3, "d")
    assert cy.items == "a e b d c".split()


def test_cylon_deleting(cylon_models):
    cylon_models.pop(0)
    assert len(cylon_models) == 9
    del cylon_models[2]
    assert len(cylon_models) == 8
    cylon_models.remove("Cylon Hybrids")
    assert len(cylon_models) == 7


def test_cylon_properties(cylon_models):
    assert cylon_models.current() == "U-87 Cyber Combat Unit"
    assert cylon_models._index == 0
    assert cylon_models.next() == "Civilian Cylon"
    assert cylon_models._index == 0
    assert cylon_models.prev() == "Humanoid Cylons"
    assert cylon_models._index == 0


def test_cylon_neighbors(cylon_models):
    answer1 = [
        "Cylon Hybrids",
        "Humanoid Cylons",
        "U-87 Cyber Combat Unit",
        "Civilian Cylon",
        "Cylon War-Era Centurion",
    ]
    answer2 = ["Humanoid Cylons", "U-87 Cyber Combat Unit", "Civilian Cylon"]
    neighbors = cylon_models.stencil()
    two_neighbors = cylon_models.stencil(1)
    assert neighbors == answer1
    assert len(neighbors) == 5
    assert len(two_neighbors) == 3
    assert two_neighbors == answer2
