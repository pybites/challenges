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

import glob, os
import re

import collections

def gen_files(pat):
    """Finds all files"""

    for file in glob.glob(pat):
        yield file

def gen_lines(files):
    """Finds all lines"""
    
    for file in files:
        with open(file) as f:
            yield f.readlines()

def gen_grep(lines, pattern):
    """Analyze whether lines match a certain pattern"""
    for line in lines:
        if line.startswith(pattern):
            yield line[len(pattern):-1]

def gen_count(lines):
    """Count number of occurrences of specific patterns"""

    yield collections.Counter(line for line in lines)
        

if __name__ == "__main__":
    # call the generators, passing one to the other
    file_pattern = '../*/*.py'
    line_pattern = "import "
 
    files = gen_files(file_pattern)
    print(files)
    lines = gen_lines(files)
    print(lines)
    lines_of_interest = gen_grep(lines, line_pattern)
    print(lines_of_interest)
    counted_lines = gen_count(lines_of_interest)

    print(counted_lines)

    print(*counted_lines)

    [print(key, value) for key, value in counted_lines]
