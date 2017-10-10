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
import fnmatch
import glob
import os
import re

def gen_files(pat):
    yield from glob.glob(pat)
    # top, filepat = pat.rsplit('*/', 1)

    # for path, dirlist, filelist in os.walk(top):
    #     if path in fnmatch.filter():
    #         for name in fnmatch.filter(filelist, filepat):
    #             yield os.path.join(path, name)


def gen_lines(files):
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                yield line


def gen_grep(lines, pattern):
    for line in lines:
        if line.startswith(pattern):
            yield re.sub(pattern, '', line).rstrip()


def gen_count(lines):
    entries = {}
    for line in lines:
        entries[line] = entries.get(line, 0) + 1

    unique = [[v, k] for k, v in entries.items()]

    for entry in sorted(unique, reverse=True):
        yield '      {0} {1}'.format(entry[0], entry[1])


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../../*/*.py')
    lines = gen_lines(files)
    imports = gen_grep(lines, r'import ')
    counts = gen_count(imports)
    for count in counts:
        print(count)
