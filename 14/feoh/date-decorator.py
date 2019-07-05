from functools import wraps
import datetime


def prepend_date(func):
    '''Decorator that prepends the current datetime.now() string repr and a space.'''
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        return f"{datetime.datetime.now()} " + func(*args, **kwargs)
    return wrapper


@prepend_date
def cheeky_log(message):
    return(message)



if __name__ == '__main__':
    print(cheeky_log("ANNOUNCE - The white zone is for loading and unloading only!"))
    print(cheeky_log("NOTICE - Bring out your dead!"))
