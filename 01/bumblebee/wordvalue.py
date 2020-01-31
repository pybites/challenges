"""
wordvalue.py: Description of what wordvalue.py does.
"""

from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as fp:
        _data = fp.readlines()
    words = [word.strip('\n') for word in _data]
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    _score = [LETTER_SCORES[letter.upper()] for letter in word]
    return sum(_score)


def max_word_value(words):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    _max = 0
    if words:
        for word in words:
            __max = calc_word_value(word)
            _max = max(_max, __max)
    else:
        _max = max_word_value(load_words())
    return _max


if __name__ == "__main__":
    import unittest
    from test_wordvalue import TestWordValue
    unittest.main()
