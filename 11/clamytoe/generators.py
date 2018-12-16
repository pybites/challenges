"""
Turn the following unix pipeline into Python code using generators
$ grep ^import `ls ../../*/*py | xargs` | awk '{print $2}' | sort | uniq -c | sort -nr
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


def display_gen(generator):
    for gen in generator:
        print(gen)


def gen_files(pat):
    yield from glob.glob(pat)


def gen_lines(files):
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                yield line


def gen_grep(lines, pat):
    return (re.sub(pat, '', l).rstrip() for l in lines if l.startswith(pat))


def gen_count(lines):
    return (f'{cnt[1]:>7} {cnt[0]}' for cnt in Counter(lines).most_common())


def main():
    # call the generators, passing one to the other
    files = gen_files('../Projects/challenges/*/*.py')
    lines = gen_lines(files)
    imports = gen_grep(lines, r'import ')
    counts = gen_count(imports)

    display_gen(counts)


if __name__ == "__main__":
    main()
