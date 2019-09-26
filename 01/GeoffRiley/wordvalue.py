from pprint import pprint

from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return [word for word in f.read().splitlines()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[x.upper()] for x in word if x.isalpha()])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    words_values = {x: calc_word_value(x) for x in words}
    return max(words_values, key=lambda k:words_values[k])


if __name__ == "__main__":
    pass  # run unittests to validate
