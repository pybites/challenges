from fizzbuzz import fizz_gen, fizz_check
from pytest import raises


def test_fizz_check():
    assert fizz_check(1) == 1
    assert fizz_check(3) == 'Fizz'
    assert fizz_check(5) == 'Buzz'
    assert fizz_check(15) == 'FizzBuzz'
    with raises(ValueError):
        fizz_check('Hello')


def test_fizz_gen():
    numbers = fizz_gen(2)
    assert next(numbers) == 1
    assert next(numbers) == 2
    with raises(StopIteration):
        next(numbers)
    word = fizz_gen('World!')
    with raises(ValueError):
        next(word)
