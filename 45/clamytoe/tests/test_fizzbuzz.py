from fizzbuzz import fizz_check, num_gen
from pytest import raises


def test_fizzbuzz():
    assert fizz_check(1) == 1
    assert fizz_check(3) == 'Fizz'
    assert fizz_check(5) == 'Buzz'
    assert fizz_check(15) == 'FizzBuzz'


def test_num_gen():
    numbers = num_gen(2)
    assert next(numbers) == 1
    assert next(numbers) == 2
