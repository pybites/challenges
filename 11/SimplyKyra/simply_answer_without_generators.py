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
    return glob.glob(pat)


# Returns all the lines from all the files
def gen_lines(files):
    my_lines = []
    for file_name in files:
        with open(file_name, mode='r') as file:
            [my_lines.append(line.strip()) for line in file]
    return my_lines


# greps each file and returns anything that started with 'import '
def gen_grep(lines, pattern):
    values = []
    for line in lines:
        if line.lower().startswith(pattern):
            values.append(re.sub("^" + pattern, '', line.lower()).strip())
    return values


# returns all the counted items from biggest to smallest
def gen_count(lines):
    return {k: v for k, v in sorted(Counter(lines).items(), reverse=True, key=lambda item: item[1])}

if __name__ == "__main__":
    # calls the methods, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    grepped_list = gen_grep(lines, "import ")
    for key, value in gen_count(grepped_list).items():
        print(f"{value} {key}")
