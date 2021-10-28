from pytest import raises

from fizzbuzz import fizzbuzz


def test_raises_type_error_for_empty_arg():
    with raises(TypeError):
        fizzbuzz()

def test_raises_value_error_for_non_number():
    with raises(ValueError):
        fizzbuzz("a")

def test_returns_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_returns_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_returns_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def test_returns_value_given_number():
    assert fizzbuzz(91) == 91