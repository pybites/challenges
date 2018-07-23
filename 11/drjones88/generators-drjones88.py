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
    for file in glob.glob(pat):
        yield file


def gen_lines(files):
    for file in files:
        with open(file) as fin:
            for line in fin.readlines():
                yield line

def gen_grep(lines, pattern):
    for line in lines:
        exp = re.match(pattern, line)
        if exp:
            yield line

def gen_count(lines):
    imports = [line.split()[1] for line in lines]
    cnt = Counter(imports)
    return cnt


def main():
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    keep_lines = gen_grep(lines, '^import')
    count = gen_count(keep_lines)
    for k, v in count.items():
        print(f'{v} {k}')

if __name__ == "__main__":
    main()
