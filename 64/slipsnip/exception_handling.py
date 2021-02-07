from functools import wraps

def handle_exceptions(callback):
    @wraps(callback)
    def handler(*args, **kwargs):
        try:
            return callback(*args, **kwargs)
        except ValueError as error:
            print(error)
            raise ValueError
    return handler
