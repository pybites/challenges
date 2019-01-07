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
import glob
import ast
from collections import namedtuple, defaultdict

Import = namedtuple("Import", ["module", "name", "alias"])


def main():
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    for file_gen in files:
        imports = gen_lines(file_gen)
        imports = get_result(imports)
        print_import_results(imports)


def gen_files(pat):
    yield glob.glob(pat)


def gen_lines(files):
    for file in files:
        with open(file) as fh:
            # https://stackoverflow.com/questions/9008451/python-easy-way-to-read-all-import-statements-from-py-module
            root = ast.parse(fh.read(), file)

        for node in ast.iter_child_nodes(root):
            if isinstance(node, ast.Import):
                module = []
            elif isinstance(node, ast.ImportFrom):
                module = node.module.split('.')
            else:
                continue

            for n in node.names:
                yield Import(module, n.name.split('.'), n.asname)


def get_result(lines):
    # TODO : How to convert to a dict comprehension
    d = defaultdict(lambda: 0)
    for line in lines:
        d[line.name[0]] += 1
    return d


def print_import_results(results):
    sorted_results = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
    for desc, cnt in sorted_results:
        msg = f'{cnt} {desc}'
        print(msg)


if __name__ == "__main__":
    main()
