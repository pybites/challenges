import generators
from collections import Counter
from itertools import islice

FILE_PATTERN = '*.py'
LINE_PATTERN = "import "

def test_gen_files():
    expected_files = ["test_generators.py", "generators.py"]

    assert list(generators.gen_files(FILE_PATTERN)) == expected_files

def test_gen_lines():
    expected_lines = ['import generators\n',
                      'from collections import Counter\n', 
                      'from itertools import islice\n',
                      '\n', 
                      "FILE_PATTERN = '*.py'\n", 
                      'LINE_PATTERN = "import "\n', 
                      ]

    test_files = ["test_generators.py"]

    assert list(generators.gen_lines(test_files))[:6] == expected_lines


def test_gen_grep():
    lines = ['import generators\n', 
             '\n', 
             "FILE_PATTERN = '*.py'\n", 
             'LINE_PATTERN = "import "\n', 
             '\n',
             ]

    expected_lines = ["generators"]

    assert list(generators.gen_grep(lines, LINE_PATTERN)) == expected_lines

def test_gen_count():

    lines = ["generators", "numpy", "generators"]

    expected_counts = [Counter({'generators': 2, 'numpy': 1})]

    assert list(generators.gen_count(lines)) == expected_counts

def test_integrated():

    expected_counter = Counter({'re': 8, 'glob': 6, 'collections': 2, 'sys': 1, 'glob, os': 1, 'generators': 1, 'ast': 1})

    files = generators.gen_files("../*/*.py")

    lines = generators.gen_lines(files)
    lines_of_interest = generators.gen_grep(lines, LINE_PATTERN)
    counted_lines = generators.gen_count(lines_of_interest)

    assert list(counted_lines)[0] == expected_counter