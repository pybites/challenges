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
from collections import Counter, defaultdict


def gen_files(pat):
    yield from glob.glob(pat)


def gen_lines(files):
    for file in files:
        with open(file) as fin:
            for line in fin.readlines():
                yield line


def gen_grep(lines, pattern):
    for line in lines:
        if line.startswith(pattern):
            yield re.sub(pattern, '', line).strip()


def gen_count(lines):
    # cnt = Counter(lines)
    # return cnt.most_common()
    results = defaultdict()
    for line in lines:
        results[line] = results.get(line, 0) + 1
    final = [[value, key] for key, value in results.items()]

    for item in sorted(final, reverse=True):
        yield item


if __name__ == "__main__":
    files = gen_files('../../*/*.py')
    lines = gen_lines(files)
    grep = gen_grep(lines, r'import ')
    counter = gen_count(grep)
    # for item in counter:
    #     print(f'{item[1]} {item[0]}')
    for item in counter:
        print(f'   {item[0]} {item[1]}')
