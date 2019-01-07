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
    yield from glob.glob(pat)


def gen_lines(files):
    for each in files:
        with open(each) as f:
            for line in f.readlines():
                yield line


def gen_grep(lines, pattern):
    # return [re.sub(pattern, '', l).rstrip()
            # for l in lines if l.startswith(pattern)]
    return [l.split()[1].rstrip() for l in lines if l.startswith(pattern)]


def gen_count(lines):
    return Counter(lines).most_common()


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    imports = gen_grep(lines, r'import ')
    counts = gen_count(imports)

    print(counts)
