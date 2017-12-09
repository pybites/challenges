def check_value(value):
    """
    Validates the value that was passed into the program.

    :param value: A positive integer is the only valid value
    :return: int or an exception is raised
    """
    if isinstance(value, bool):
        raise ValueError
    elif isinstance(value, str):
        raise ValueError
    elif isinstance(value, float):
        raise ValueError
    elif value <= 0:
        raise ValueError
    else:
        try:
            tested_value = int(value)
            return tested_value
        except ValueError:
            raise ValueError
        except TypeError:
            raise TypeError


def fizz_check(num):
    """
    Determines the correct FiiBuzz value to return for the int given.

    If the number is divisible by 3 'Fizz' is returned.
    If the number is divisible by 5 'Buzz' is returned.
    If the number is divisible by both 3 and 5, 'FizzBuzz' is returned.
    If none of those are true, then number is just returned.

    :param num: A positive integer
    :return: 'Fizz', 'Buzz', 'FizzBuzz', or the num given
    """
    value = check_value(num)
    return 'Fizz' * (value % 3 == 0) + 'Buzz' * (value % 5 == 0) or value


def fizz_gen(limit):
    """
    FizzBuzz generator.

    :param limit: An integer representing the last number to be processed
    :return: Integer or String returned after going through fizz_check()
    """
    max_num = check_value(limit)
    for num in range(1, max_num + 1):
        yield fizz_check(num)


def fizzbuzz(limit=100):
    """
    Super overcomplicated implementation of the FizzBuzz challenge.

    :param limit: Default value of numbers to process
    :return: Standard Out response after being processed
    """
    value = check_value(limit)
    gen = fizz_gen(value)
    for _ in range(value):
        print(next(gen))


if __name__ == '__main__':
    fizzbuzz()
