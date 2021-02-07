import glob
import re
from collections import Counter

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


# Uses glob to grab all the filenames in the pathway (pat) given
def gen_files(pat):
    for filename in glob.glob(pat):
        yield filename


# Returns all the lines from all the files
def gen_lines(files):
    for file_name in files:
        with open(file_name, mode='r') as file:
            yield [line.strip() for line in file]


# greps each file and returns anything that started with 'import '
def gen_grep(lines, pattern):
    values = []
    for my_lines in lines:
        for line in my_lines:
            if line.lower().startswith(pattern):
                yield re.sub("^" + pattern, '', line.lower()).strip()


# returns all the counted items from biggest to smallest
def gen_count(lines):
    lines = sorted(Counter(lines).items(), reverse=True, key=lambda item: item[1])
    for k,v in lines:
        yield k,v

if __name__ == "__main__":
    # calls the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    grepped_list = gen_grep(lines, "import ")
    for key, value in gen_count(grepped_list):
        print(f"{value} {key}")

