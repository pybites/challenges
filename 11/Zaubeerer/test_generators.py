import generators

FILE_PATTERN = '../*/*.py'
LINE_PATTERN = "import "

def test_gen_files():
    expected_files = "..."

    assert generators.gen_files(FILE_PATTERN) == expected_files

def test_gen_lines():
    expected_lines = "..."

    test_files = "filename"

    # test_lines = test_files.readlines() # pseudocode

    assert generators.gen_lines(test_files) == test_lines


def test_gen_grep():
    lines = " ..."

    expected_lines = "..."

    assert generators.gen_grep(lines, LINE_PATTERN) == expected_lines

def test_gen_count():

    lines = "..."

    expected_counts = "..."

    assert generators.gen_count(lines) == expected_counts