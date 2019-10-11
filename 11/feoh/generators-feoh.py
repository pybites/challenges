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

from glob import iglob
from collections import defaultdict
import re

def gen_files(pat):
    for fm in iglob(pat):
        yield(fm)


def gen_lines(files):
    for file in files:
        with open(file,'r') as f:
            yield(f.readline())


def gen_grep(lines, pattern):
    found_lines = [ line.strip() for line in lines if re.match(pattern, line) ]
    for line in found_lines:
        yield(line)


def gen_sed(lines, pattern, replacement):
   filtered_lines = [ re.sub(pattern, replacement, line) for line in lines ]
   for line in filtered_lines:
       yield(line)


def gen_count(lines):
    linecounts = defaultdict(int)

    for line in lines:
        linecounts[line] = linecounts[line] + 1

    for count in linecounts.keys():
        yield(f"{linecounts[count]} {count}")


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    found_lines = gen_grep(lines, '^import')

    filtered_lines = []

    for line in gen_sed(found_lines, '^import', ''):
        filtered_lines.append(line)

    for count in gen_count(filtered_lines):
        print(count)
