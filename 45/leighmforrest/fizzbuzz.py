def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if not n % 3:
        return 'Fizz'
    if not n % 5:
        return 'Buzz'
    return n

