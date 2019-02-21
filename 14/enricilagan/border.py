from functools import wraps, partial


def get_border(func=None, count=10):
    """Decorators that adds border before and after the function return (works with strings)"""
    if func is None:
        return partial(get_border, count=count)
    count = count if count else 2

    @wraps(func)
    def wrapper(*args, **kwargs):
        return ('==' * count) + '\n\n' + func(*args, **kwargs) + '\n\n' + ('==' * count) + '\n'
    return wrapper