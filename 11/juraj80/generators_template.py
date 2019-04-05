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
from pathlib import Path
import re
from collections import Counter

def gen_files(pat):
    for filename in Path(path).rglob('*.py'):
        yield open(filename, 'r')

def gen_lines(files):
    for file in files:
        yield from file

def gen_grep(lines, pattern):
    patc = re.compile(pattern)
    return (line for line in lines if patc.search(line))

def gen_count(lines):
    return Counter(lines).most_common(5)


if __name__ == "__main__":
    # call the generators, passing one to the other
    pattern = r'^import'
    path = "/"

    files = gen_files(path)
    lines = gen_lines(files)
    patlines = gen_grep(lines, pattern)
    import_string = (line.split()[1] for line in patlines)
    for key, value in gen_count(import_string):
        print(value, key)
