#https://codechalleng.es/challenges/11/
#http://www.dabeaz.com/generators/
#https://en.wikipedia.org/wiki/Pipeline_(Unix)
#https://pybit.es/codechallenge11.html

# The Script finds all python files from the root directoty
# Searches for the word import as the first word in a line
# returns that line and removes the 'import '.
# Basically, it collects all imported modules.
# The command then sorts them and counts the occurences.
# The module sare then sorteb by ovvurence frecuency.
# The question is: in your python files, sort all imported modules from 
# more used to least used.

import os
import re
import glob
from collections import Counter


def get_python_files(path):
    yield from glob.glob(path)


def file_line_by_line(file):
    with open(file) as f:
            for line in f.readlines():
                print(file)
                yield line


def all_lines(py_files):
    for file_ in py_files:
        yield from file_line_by_line(file_)

def find_modules(lines, modules):
    pattern = re.compile(r'import[\s][A-Za-z0-9]+')
    [modules.append(line[re.search(pattern, line).span()[0] : re.search(pattern, line).span()[1]].replace('import' ,'').strip()) for line in lines if re.search(pattern, line) != None]

         


def get_all_instances(file_text, modules):
    while True:
        try:
            find_modules(next(file_text), modules)
        except StopIteration:
            return modules


def final_print(modules):
    cnt = Counter(modules)
    [print(item[1], item[0]) for item in cnt.most_common()]
    


def main():
    py_files = get_python_files('../*/*.py')
    code_lines = all_lines(py_files)
    # file_text = get_file_text(python_files)
    # modules = get_all_instances(file_text ,modules)
    # final_print(modules)


if __name__ == "__main__":
    main()