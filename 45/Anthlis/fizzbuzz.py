def fizzbuzz(num):
    """
    Evaluates if a number is a multiple of 3, of 5 or both.
    Args:
        num: The number to evaluate for "FizzBuzz". Must be an integer.
    Returns:
        str: "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of 3 and 5, otherwise num.
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    if not num % 3:
        return 'Fizz'
    if not num % 5:
        return 'Buzz'
    return num


def main():
    """Prints the return of fizzbuzz for numbers 1 to 100."""
    for i in range(1, 101):
        print(i, fizzbuzz(i))


if __name__ == '__main__':
    main()

