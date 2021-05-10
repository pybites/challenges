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
from glob import iglob
import re


def gen_files(pat):
    yield from iglob(pat)


def gen_lines(files):
    for fi in files:
        with open(fi) as f:
            yield from f.readlines()


def gen_grep(lines, pattern):
    for line in lines:
        m = pattern.match(line.rstrip())
        if m:
            yield m.group(1)


def gen_count(modules):
    yield from Counter(modules).most_common()


if __name__ == "__main__":
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    modules = gen_grep(lines, re.compile(r'^import (\w+)'))
    for mod, count in gen_count(modules):
        print('{:<2} {}'.format(count, mod))
