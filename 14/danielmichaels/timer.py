import time
from functools import wraps

import requests
from tqdm import tqdm


def timer(function):
    """
    Timer decorator for return a functions execution in seconds.
    Args:
        function: function to be timed
    Returns: time taken plus the original function executed.
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = function(*args, **kwargs)
        print(
            f"[*] {function.__name__} completed in {time.time() - t1:.2f} seconds [*]"
        )
        return result

    return wrapper


@timer
def download_test():
    """ Download a test file for assessing speed."""
    url = "http://speedcheck.cdn.on.net/10meg.test"
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024
    t = tqdm(total=total_size, unit="iB", unit_scale=True)
    with open("test.file", "wb") as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()


if __name__ == "__main__":
    download_test()
