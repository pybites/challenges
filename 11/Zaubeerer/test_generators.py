from collections import Counter
from itertools import islice

import generators

FILE_PATTERN = "*.py"
LINE_PATTERN = "import "


def test_gen_files():
    expected_files = ["test_generators.py", "generators.py"]
    actual_files = list(generators.gen_files(FILE_PATTERN))

    assert actual_files == expected_files


def test_gen_lines():
    expected_lines = [
        "from collections import Counter\n",
        "from itertools import islice\n",
        "\n",
        "import generators\n",
        "\n",
        'FILE_PATTERN = "*.py"\n',
        'LINE_PATTERN = "import "\n',
    ]
    test_files = ["test_generators.py"]
    actual_files = list(generators.gen_lines(test_files))[:7]

    assert actual_files == expected_lines


def test_gen_grep():
    lines = [
        "import generators\n",
        "\n",
        "FILE_PATTERN = '*.py'\n",
        'LINE_PATTERN = "import "\n',
        "\n",
    ]
    expected_lines = ["generators"]
    actual_files = list(generators.gen_grep(lines, LINE_PATTERN))

    assert actual_files == expected_lines


def test_gen_count():
    lines = ["generators", "numpy", "generators"]
    expected_counts = [Counter({"generators": 2, "numpy": 1})]
    actual_counts = list(generators.gen_count(lines))

    assert actual_counts == expected_counts


def test_integrated():

    expected_counter = Counter(
        {
            "re": 8,
            "glob": 7,
            "collections": 2,
            "sys": 1,
            "os": 1,
            "generators": 1,
            "ast": 1,
        }
    )

    files = generators.gen_files("../*/*.py")

    lines = generators.gen_lines(files)
    lines_of_interest = generators.gen_grep(lines, LINE_PATTERN)
    counted_lines = generators.gen_count(lines_of_interest)

    actual_counter = list(counted_lines)[0]

    assert actual_counter == expected_counter
