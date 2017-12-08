from fizzbuzz import fizzbuzz, num_gen
from pytest import raises


def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'


def test_num_gen():
    numbers = num_gen(2)
    assert next(numbers) == 1
    assert next(numbers) == 2
