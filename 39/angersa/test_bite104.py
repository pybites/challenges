from bite104 import split_in_columns

def test_split_in_columns():
    expected = "Hello world!|We hope that you are learning a lot of Python.|Have fun with our Bites of Py.|Keep calm and code in Python!|Become a PyBites ninja!"

    assert split_in_columns() == expected


def test_on_other_string():
    message = "Hi!\nMy name is Annie\nI suck at testing so far."

    expected = "Hi!|My name is Annie|I suck at testing so far."

    assert split_in_columns(message) == expected
