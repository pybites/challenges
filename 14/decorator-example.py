from functools import wraps
from time import sleep


def uppercase(func):
    '''Decorator that uppercases func, no args'''
    @wraps(func)  # preserves function meta data
    def wrapper():
        return func().upper()
    return wrapper


def sleep_decorator(func):
    '''Decorator that sleeps n seconds, passes through args'''
    interval = 2
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Sleep {interval} seconds')
        sleep(interval)
        return func(*args, **kwargs)
    return wrapper


@uppercase
def hello_world():
    return 'hello world'


@sleep_decorator
def print_word(word):
    '''Print a word'''
    print(word)


if __name__ == '__main__':
    print('1. Printing "hello world" to upper with decorator:')
    print(hello_world())

    print()
    print('2. Sleep n seconds before calling func:')

    words = 'today is a great pythonic day'.split()

    for w in words:
        print_word(w)
