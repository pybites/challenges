"""
Turn the following unix pipeline into Python code using generators
$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

import re
import sys
from pathlib import Path
from collections import Counter


def gen_files(pat):
    """
    Receives a pattern and yields a file path from a Path list
    for all matching files
    """
    cur_path = Path(".")
    file_paths = cur_path.glob(pat)
    yield from file_paths


def gen_lines(files):
    """
    Receives an iterator of Paths and will
    read and return each line after each
    other.
    """
    for file in files:
        with file.open(encoding="utf-8") as f:
            line = f.readline()
            while line:
                yield line
                line = f.readline()


def gen_grep(lines, pattern):
    """
    Looks up if regex pattern is in lines and will
    yield every match. The pattern has either no
    capturing group (everything will be matched) or
    one capturing group, which will be yielded.
    """
    reg_expr = re.compile(pattern)
    if reg_expr.groups > 1:
        print(
            "This function needs a pattern with either no capturing group, "
            "i.e. for a complete match or it takes an expression with a single group, "
            "which will be returned instead of the complete match."
        )
        print("The program will now halt.")
        sys.exit(-1)

    yield_group = 0 if reg_expr.groups == 0 else 1

    for line in lines:
        for match in reg_expr.finditer(line):
            if match is not None:  # finditer includes empty matches
                yield match.group(yield_group)


def gen_count(lines):
    """
    Takes an iterable as input and yields the most common elements
    in descending order, encoded in a tuple with the element and the count
    as elements.
    """
    cnt = Counter(lines)  # Counter works on iterables and is not memory heavy
    yield from cnt.most_common()  # most_common sorts them descending


def print_results(cnt_tuple):
    """
    Takes the output of gen_count as an input and
    displays it neatly.
    """
    for elem, count in cnt_tuple:
        print(f"\t{count} {elem}")


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files("../*/*py")
    lines = gen_lines(files)
    grep_results = gen_grep(lines, r"^import (\w+)")
    count_tuples = gen_count(grep_results)
    print_results(count_tuples)
