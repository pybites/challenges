def check_value(value):
    if isinstance(value, bool):
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
    value = check_value(num)
    return 'Fizz' * (value % 3 == 0) + 'Buzz' * (value % 5 == 0) or value


def fizz_gen(limit=100):
    max_num = check_value(limit)
    for num in range(1, max_num + 1):
        yield fizz_check(num)


def fizzbuzz(limit=100):
    value = check_value(limit)
    gen = fizz_gen(value)
    for _ in range(value):
        print(next(gen))


if __name__ == '__main__':
    fizzbuzz()
