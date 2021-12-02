# -*- coding: utf-8 -*-
from numbers import Number
from typing import Union


def fizzbuzz(val: Number) -> Union[str, Number]:
    if not isinstance(val, Number) or val % 1 != 0:
        raise ValueError('Only whole integer values accepted')
    if val % 15 == 0:
        return "FizzBuzz"
    if val % 5 == 0:
        return "Buzz"
    if val % 3 == 0:
        return "Fizz"
    return val

    # Playing FizzBuzz
    #   when passed the value 3
    #     ✓ it says "Fizz"
    #   when passed a multiple of 3
    #     ✓ it says "Fizz"
    #   when passed the value 5
    #     ✓ it says "Buzz"
    #   when passed a multiple of 5
    #     ✓ it says "Buzz"
    #   when passed a multiple of 3 and 5
    #     ✓ it says "FizzBuzz"
    #   when passed a value divisible by neither 3 nor 5
    #     ✓ it says the value back unchanged
    #   when passed a none whole integer value
    #     ✓ it screams and raises a ValueError
    #   when pass a none numeric value
    #     ✓ it screams and raises a ValueError
