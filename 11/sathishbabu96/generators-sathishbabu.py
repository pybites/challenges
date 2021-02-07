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


def gen_files(path):
    return glob.iglob(path)


def gen_lines(files):
    for file in files:
        with open(file, 'r') as fptr:
            yield fptr.readline()


def gen_grep(lines, pattern):
    for line in lines:
        result = re.match(pattern, line)
        if result:
            yield line


def gen_count(lines):
    counter = Counter()
    for line in lines:
        word = line.strip('\n').split(' ')[1]
        counter[word] += 1
    return counter.most_common()


if __name__ == "__main__":

    files = gen_files('../c11/*.py')
    lines = gen_lines(files)
    lines_import = gen_grep(lines, r'import [\w]+')
    for key, value in gen_count(lines_import):
        print(f'{value:<12}{key}')
