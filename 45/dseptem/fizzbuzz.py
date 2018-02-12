def fizzbuzz(num):
    """Evaluates if a number is a multiple of 3, of 5 or both.

    Args:
        num: The number to evaluate for "FizzBuzz". Must be an integer, or an integer as a string.

    Returns:
        str: "Fizz" for multiples of 3, "Buzz" for mults of 5, "FizzBuzz" for mults of 3 and 5, otherwise num.
    """
    if isinstance(num, float):
        raise ValueError
    try:
        num = int(num)
    except ValueError as e:
        raise e

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num


def display_fizzbuzz(num):
    """Prints the "FizzBuzz" of a number.

    Args:
        num: The integer to be printed after going through the fizzbuzz function.

    Returns:
        None: Only prints to stdout.
    """
    if isinstance(num, float):
        raise ValueError
    try:
        num = int(num)
    except ValueError as e:
        raise e

    print(fizzbuzz(num))


def main():
    """Prints the return of fizzbuzz for numbers from 1 to 100."""
    for i in range(1,101):
        display_fizzbuzz(i)


if __name__ == '__main__':
    main()
