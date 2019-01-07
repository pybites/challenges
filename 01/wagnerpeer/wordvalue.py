from collections import defaultdict

from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as fid:
        words = [line.rstrip() for line in fid]

    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[character] for character in word.upper()
                if 65 <= ord(character) <= 90])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_values = defaultdict(list)
    if words is None:
        words = load_words()

    for word in words:
        word_values[calc_word_value(word)].append(word)

    return sorted(word_values[max(word_values)])[0]


if __name__ == "__main__":
    pass # run unittests to validate
