def fizzbuzz(number):
    """
    Convert a number to its FizzBuzz equivalent string:

        * "Fizz" if `number` is a multiple of 3
        * "Buzz" if `number` is a multiple of 5
        * "FizzBuzz" if `number` is a multiple of both 3 and 5
        * `number` as a string if not a multiple of 3 nor 5

    :param number: Integer number to evaluate.
    :return: "FizzBuzz", "Fizz", "Buzz" or the number as string.
    """
    if not isinstance(number, int):
        raise ValueError("Expecting to process an integer.")

    is_fizz = number % 3 == 0
    is_buzz = number % 5 == 0

    if is_fizz and is_buzz:
        return "FizzBuzz"
    if is_fizz:
        return "Fizz"
    if is_buzz:
        return "Buzz"

    return str(number)


def fizzbuzz_100():
    return ", ".join(map(fizzbuzz, range(1, 101)))


def main():
    print(fizzbuzz_100())


if __name__ == '__main__':
    main()
