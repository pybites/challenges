from functools import wraps


def trace_log(level=None):
    def real_decorator(func):
        """Decorator to trace func execution and optionally parameters"""

        @wraps(func)  # preserves function meta data
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            if level == "verbose":
                print(f"Executing: {func_name} with parameters {args} {kwargs}")
            else:
                print(f"Executing: {func_name}")
            cmd = func(*args, **kwargs)
            print(f"Done executing {func_name}")
            return cmd

        return wrapper

    return real_decorator


@trace_log()
def print_message(message, num_times=1):
    for i in range(num_times):
        print(message)


if __name__ == "__main__":
    print_message("Hello, word!", num_times=3)
