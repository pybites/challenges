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
import glob
import re
from collections import Counter


def gen_files(pat):
    yield from glob.glob(pat)


def gen_lines(files):
    for filepath in files:
        with open(filepath, 'r') as file:
            yield from file.readlines()


def gen_grep(lines, pattern):
    regex = re.compile(pattern)
    for line in lines:
        if regex.match(line):
            yield regex.sub("", line).strip()


def gen_count(lines):
    yield from sorted(Counter(lines).items(), key=lambda pair: (pair[1], pair[0]), reverse=True)

if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    imports = gen_grep(lines, "^import")
    counts = gen_count(imports)
    for k, v in counts:
        print(v, k)
