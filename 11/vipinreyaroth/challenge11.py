import glob
import re
from collections import Counter

"""
Turn the following unix pipeline into Python code using generators
$ for i in ../*/*.py; do grep ^import |sed '/s/import //s' ; done | sort | uniq -c | sort -nr
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


def gen_files(pattern):
    for file in glob.glob(pattern):
        yield file


def gen_lines(files):
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                yield line


def gen_grep(lines, pattern):
    for line in lines:
        match = re.match(pattern, line)

        if match:
            yield line


def gen_count(lines):
    imports = (line.split()[1] for line in lines)
    count = Counter(imports)
    unique = ([v, k] for k, v in count.items())

    for entry in sorted(unique, key=lambda x: x[0], reverse=True):
        yield f'{entry[0]} {entry[1]}'


def main():
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    lines_with_imports = gen_grep(lines, '^import ')
    counts = gen_count(lines_with_imports)

    for count in counts:
        print(count)


if __name__ == '__main__':
    main()
