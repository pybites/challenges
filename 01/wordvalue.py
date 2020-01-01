from data import DICTIONARY, LETTER_SCORES
import string
from functools import reduce


def load_words():
    """Load dictionary into a list and return list"""
    file = open(DICTIONARY, "r")
    words = [i.replace("\n", "") for i in file.readlines()]
    file.close()
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[i.upper()] for i in word if i in string.ascii_letters)


def max_word_value(word_list = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list is None:
        word_list = load_words()
    scores = {i: calc_word_value(i) for i in word_list}
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[0][0]


if __name__ == "__main__":
    pass # run unittests to validate
