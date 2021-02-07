import time
from functools import wraps


string = 'There is nothing like a challenge to bring out the best in man'

def uppercase(func):
    @wraps(func)
    def wrapper_upper(arg):
        return func(arg).upper()
    return wrapper_upper

def sleeper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Something before')
        time.sleep(1)
        print(f'Start the function {func.__name__}()')
        func(*args, **kwargs)
        print(f'{func.__name__}() is finished')
        print('Something after')
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper


@sleeper
@uppercase
def return_str(text):
    return text

if __name__ == '__main__':
    k = return_str(string)
    print(k)