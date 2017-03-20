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
from collections import Counter
import glob
import re


def gen_files(pat):
    for file_path in glob.glob(pat):
        yield file_path


def gen_lines(files):
    for fi in files:
        with open(fi) as f:
            for line in f.readlines():
                yield line.strip()


def gen_grep(lines, pattern):
    for line in lines:
        m = pattern.match(line)
        if m:
            yield m.group(1)


def gen_count(lines):
    for count in Counter(lines).most_common():
        yield count


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    lines = gen_grep(lines, re.compile(r'^import (\w+)'))
    counts = gen_count(lines)
    for mod, count in counts:
        print('{:<2} {}'.format(count, mod))
