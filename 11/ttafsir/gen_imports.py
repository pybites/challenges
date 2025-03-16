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
import re
from pathlib import Path
from collections import Counter


GREP_PATTERN = re.compile(r"^import\s(.*)")
GLOB_PATTERN = "../../*/*.py"


def gen_files(pat: str):
    """Glob directory and return generator"""
    return Path(".").glob(pat)


def gen_lines(files):
    """yield lines from filepaths"""
    for path in files:
        yield from path.read_text().splitlines()


def gen_grep(lines, pattern):
    """search for pattern in lines"""
    for ln in lines:
        match = re.search(pattern, ln)
        if match:
            yield match.group(1)


def gen_count(lines):
    """return the sorted count of line found imports"""
    c = Counter(lines)
    for elem, count in c.most_common():
        yield f"{count:>4} {elem}"


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files(GLOB_PATTERN)
    lines = gen_lines(files)
    lines = gen_grep(lines, GREP_PATTERN)

    for ln in gen_count(lines):
        print(ln)
