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
    yield from glob.glob(pat, recursive=True)

def gen_lines(files):
    for f in files:
        with open(f, "r") as file:
            yield from file.readlines()

def gen_grep(lines, pattern):
    p = re.compile(pattern)
    for line in lines:
        if p.search(line):
            yield p.sub("", line)

def gen_count(lines):
    return sorted(Counter(lines).items(), key=lambda pair: (pair[1], pair[0]), reverse=True)


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    greps = gen_grep(lines, "^import")
    # etc
    counts = gen_count(greps)
    for key, val in counts:
        print (str(val) + " " + key)
