from functools import wraps
from pprint import pprint


def check_input(func):
    '''Decorator to print the arguments passed to a function'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        out = func(*args, **kwargs)
        if args:
            print(f'\nTRACE: calling {func.__name__}() '
                  f'with args = ')
            pprint(f'{args} ')
            print(f'and kwargs = {kwargs}\n')
        else:
            print(f'\nTRACE: calling {func.__name__}() '
                  f'with default values\n')
        return out
    return wrapper


@check_input
def print_text(text='I code with PyBites!'):
    return text


if __name__ == "__main__":
    print_text()
    text = 'Hello!'
    print_text(text)
