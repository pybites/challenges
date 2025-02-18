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
from pathlib import Path


def gen_files(pat):
    yield from Path('.').glob(pat)


def gen_grepped_lines(file_gen):
    for fn in file_gen:
        with fn.open() as f:
            yield from [line
                        for line in f.read().splitlines(keepends=False)
                        if line.startswith('import')]


def gen_sed(line_gen):
    """
    This could theoretically process a bunch of 'sed' commands,
    however, for this case it is programmed with the fixed instance.
    """
    yield from [line.replace('import ', '') for line in line_gen]


def gen_count(line_gen):
    counts = Counter(module for line in line_gen for module in line.split(','))
    return [f'{v:>2} {k}' for k, v in counts.most_common()]


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_grepped_lines(files)
    edited_lines = gen_sed(lines)
    summary = gen_count(edited_lines)

    print('\n'.join(summary))
