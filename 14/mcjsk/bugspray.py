from functools import wraps


def bugspray(verbosity=1):
    """Print wrapped function metadata—function name, parameters, & arguments
    —to stdout, and, optionally log same to file by increasing verbosity"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kws):
            metadata = f"function: {func.__name__}\nparams [{func.__code__.co_argcount}]: {func.__code__.co_varnames}\nargs [pos|kw]: {args}, {kws}"
            if verbosity > 1:
                with open(f"{func.__name__}_log.txt", "w") as f:
                    f.write(str(metadata) + "\n")
            if verbosity > 0:
                print(f"\33[35m{metadata}\033[0m")
            func(*args, **kws)

        return wrapper

    return decorator


@bugspray(2)
def csvrep(report, data):
    with open("temp.txt", "w") as f:
        f.write(f"Report: {report}\ndata\n")


csvrep("testreport", "testdata")
