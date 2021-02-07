from functools import wraps


def your_decorator(func):
    '''Decorator to ...'''
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        # do stuff before func
        return func(*args, **kwargs)
        # do stuff after func
    return wrapper


@your_decorator
def some_function():
    pass


if __name__ == '__main__':
    some_function()
