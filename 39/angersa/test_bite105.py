from bite105 import text, slice_and_dice

other_text = """
Take the block of text provided and strip off the whitespace at both ends. Split the text by newline (\n).
Loop through the lines, for each line:
strip off any leading spaces,
check if the first character is lowercase,
if so, split the line into words and get the last word,
strip the trailing dot (.) and exclamation mark (!) from this last word,
and finally add it to the results list.
Return the results list."""

def test_slice_and_dice():
    expected = ['objects', 'y', 'too', ':)', 'bites']
    assert slice_and_dice() == expected


def test_other_text():
    expected = ['spaces,', 'lowercase,', 'word,', 'word,', 'list']
    assert slice_and_dice(other_text) == expected

