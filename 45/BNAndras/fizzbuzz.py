#!/usr/bin/env python3

from typing import Union

def fizzbuzz(n: int) -> Union[str, int]:
    if not isinstance(n, int):
        raise ValueError("Passed value is not a number.")

    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n
