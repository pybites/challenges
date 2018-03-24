from functools import wraps, partial
import logging
from random import random
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',  # noqa E501
                    datefmt='%H:%M:%S',
                    filename='decorators.log',
                    filemode='a')


def timeit(func):
    """a simple one - from Python cookbook 3rd ed"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print()
        print(f'{func.__name__} of args: {args} took {end-start}')
        return result
    return wrapper


def mute_exception(func=None, *, reraise=False, default_return=None):
    """Technique:
       http://pybit.es/decorator-optional-argument.html
       (Python cookbook 3rd ed)
       Inspiration: https://www.blog.pythonlibrary.org/2016/06/09/
       python-how-to-create-an-exception-logging-decorator/"""
    if func is None:
        return partial(mute_exception, reraise=reraise,
                       default_return=default_return)

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.debug(f'{func.__name__} called for args {args}')
            return func(*args, **kwargs)
        except Exception as e:
            exc = f'{func.__name__} raised exception \
                    {e.__class__.__name__} for args: {args}'
            logging.error(exc)
            if reraise:
                raise
            return default_return
    return wrapper


if __name__ == '__main__':

    # decorator to time the operation
    @timeit
    # second (stacked decorator)
    # works: no args provided = takes defaults (no reraise, returns None)
    # @mute_exception
    # works: raises the ZeroDivisionError = crash
    # @mute_exception(reraise=True)
    # works: does not reraise ZeroDivisionError and returns 0 in that case
    @mute_exception(reraise=False, default_return=0)
    def div(i, j):
        # take a bit of time to make timeit useful
        time.sleep(random())
        return i/j

    a = (1, 2, 3)
    # last element triggers ZeroDivisionError
    b = (4, 5, 0)

    for i, j in zip(a, b):
        res = div(i, j)
        print(f'div {i}/{j} = {res}')
