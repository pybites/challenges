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

def gen_files(pat):
    yield from glob.glob(pat)

def gen_lines(files):
    for filename in files:
        with open(filename) as f:
            yield from f

def gen_grep(lines, pattern):
    yield from [l.split()[1] for l in lines if l.startswith(pattern)]

def gen_count(lines):
    yield from collections.Counter(lines).most_common()


if __name__ == "__main__":
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    matches = gen_grep(lines, 'import')
    result = gen_count(matches)
    for mod, cnt in result:
        print(f'{cnt:^3} {mod}')