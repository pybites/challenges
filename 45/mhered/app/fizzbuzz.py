#!/usr/bin/python3


def fizzbuzz(num: int):
    """
    FizzBuzz(int) plays FizzBuzz
    """
    if not isinstance(num, int):
        raise ValueError("argument should be of type int")
    else:
        if num % 5 == 0 and num % 3 == 0:
            return "FizzBuzz"
        if num % 5 == 0:
            return "Buzz"
        if num % 3 == 0:
            return "Fizz"
        return num
