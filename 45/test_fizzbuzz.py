import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("number", [3, 6, 9, 12, 18, 21, 24, 27, 33])
def test_three(number):
    assert fizzbuzz(number) == 'Fizz'


@pytest.mark.parametrize("number", [5, 10, 20, 25, 35, 40, 50, 55, 80, 95])
def test_five(number):
    assert fizzbuzz(number) == 'Buzz'


@pytest.mark.parametrize("number", [15, 30, 45, 60, 75, 90])
def test_fifteen(number):
    assert fizzbuzz(number) == 'FizzBuzz'


@pytest.mark.parametrize("number", [2, 8, 23, 98, 76, 58, 64, 44, 37, 38, 19])
def test_non_three_or_five(number):
    assert fizzbuzz(number) == number


def test_exception_on_boolean():
    with pytest.raises(ValueError):
        fizzbuzz(True)


def test_exception_on_float():
    with pytest.raises(ValueError):
        fizzbuzz(10.345)


def test_exception_on_number_like_string():
    with pytest.raises(ValueError):
        fizzbuzz('3')


def test_exception_on_list():
    with pytest.raises(ValueError):
        fizzbuzz([1, 2, 3])


def test_exception_on_none():
    with pytest.raises(ValueError):
        fizzbuzz(None)
