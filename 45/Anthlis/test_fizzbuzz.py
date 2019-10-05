import pytest

from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("test_input, expected",[
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
    (16, 16),
    (50, 'Buzz'),
    (60, 'Fizz Buzz'),
    (74, 74),
    (75, 'Fizz Buzz'),
    (92, 92),
    (98, 98),
    (99, 'Fizz'),
    (100, 'Buzz'),
])
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected