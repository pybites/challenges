"""
Implements the FizzBuzz protocol. Returns Fizz if number is divisible by 3,
Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5, or the number
itself otherwise.
"""

def fizzbuzz(number):
    """

    :param number: Integer to check
    :return: Fizz, Buzz, FizzBuzz, or the number
    """

    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError

    if number % 15 == 0:
        return 'FizzBuzz'
    elif number % 5 == 0:
        return 'Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    else:
        return number
