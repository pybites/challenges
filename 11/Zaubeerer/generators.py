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

import collections
import glob
import os
import re


def gen_files(pat):
    """Finds all files"""
    yield from glob.glob(pat)


def gen_lines(files):
    """Finds all lines"""
    for file in files:
        with open(file) as f:
            yield from f.readlines()


def gen_grep(lines, pattern):
    """Analyze whether lines match a certain pattern"""
    for line in lines:
        if line.startswith(pattern):
            yield line[len(pattern) : -1]


def gen_count(lines):
    """Count number of occurrences of specific patterns"""
    yield collections.Counter(line for line in lines)


if __name__ == "__main__":
    # call the generators, passing one to the other
    file_pattern = "../*/*.py"
    line_pattern = "import "

    files = gen_files(file_pattern)
    lines = gen_lines(files)
    lines_of_interest = gen_grep(lines, line_pattern)
    counted_lines = gen_count(lines_of_interest)
