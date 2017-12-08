def fizz_check(num):
    if isinstance(num, str):
        raise ValueError
    else:
        num = int(num)
        if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        else:
            return num


def fizz_gen(max_num=100):
    if isinstance(max_num, str):
        raise TypeError
    else:
        for num in range(1, max_num + 1):
            yield fizz_check(num)


def fizzbuzz(limit):
    pass


if __name__ == '__main__':
    stop_at = 15
    results = fizz_gen(stop_at)
    for _ in range(stop_at):
        print(next(results))
