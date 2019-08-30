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
from collections import Counter
from glob import glob


PATH = "../../*/*.py"
PATTERN = "import"


def gen_files(path):
    """
    generate the names of all the files in the path

    for i in ../*/*py
    """
    for file in glob(path):
        yield file


def gen_lines(files):
    """
    generate all lines from the interested files
    """
    for file in files:
        with open(file, "r") as f:
            yield from f


def gen_grep(lines, pattern):
    """
    generate cleaned and filtered out lines by pattern

    grep ^import $i|sed 's/import //g'
    """
    return (
        line.replace(pattern, "").strip(f"\n ")  # Finally strip the newlines and spaces
        for line in lines
        if line.startswith(pattern)
    )


def gen_count(lines):
    """
    output1 = Group lines by count, then sort by names
    output2 = sort output1 by count (still maintaining the sorted names)
    result = generate output2 in reverse order
    """
    uniques = Counter(lines)
    sorted_by_name = sorted(uniques.items())  # output1, a list of tuples: [('csv', 5), ...]
    sorted_by_count = sorted(sorted_by_name, key=lambda x: x[1])  # output2, a list of tuples
    yield from reversed(sorted_by_count)  # result


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files(path=PATH)
    lines = gen_lines(files=files)
    modules = gen_grep(lines=lines, pattern=PATTERN)
    for module, count in gen_count(modules):
        print(f'{" "*6}{count} {module}')


