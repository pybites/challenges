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
import collections


def gen_files(pat):
    yield from glob.glob(pat)


def gen_lines(files):
    for file in files:
        with open(file) as f:
            fil = f.readlines()
            yield from fil


def gen_grep(lin, patt):
    pattern = re.compile(patt)
    for line in lin:
        if pattern.match(line):
            yield pattern.sub("", line).strip()

def gen_count(lines):
    count = collections.Counter(lines)
    return(sorted(count.items(), key=lambda x:(x[1], x[0],), reverse=True))

if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    gengrep = gen_grep(lines, '^import')
    gg = gen_count(gengrep)
    for k,v in gg:
        print('{} {}'.format(k,v))
    # etc