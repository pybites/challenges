import generators
from collections import Counter

FILE_PATTERN = '*.py'
LINE_PATTERN = "import "

def test_gen_files():
    expected_files = ["test_generators.py", "generators.py"]

    assert list(generators.gen_files(FILE_PATTERN)) == expected_files

def test_gen_lines():
    expected_lines = ['import generators\n',
                      'from collections import Counter\n', 
                      '\n', 
                      "FILE_PATTERN = '*.py'\n", 
                      'LINE_PATTERN = "import "\n', 
                      ]

    test_files = ["test_generators.py"]

    assert list(generators.gen_lines(test_files))[0][:5] == expected_lines


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