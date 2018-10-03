from data import DICTIONARY, LETTER_SCORES
import re


def load_words():
    """Load dictionary into a list and return list"""
    file = open(DICTIONARY)
    words = file.read().splitlines()
    file.close()

    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    _word = re.findall('[A-Za-z]', word)  # only letters
    letters = [l.upper() for l in _word]
    score = sum(LETTER_SCORES[l] for l in letters)
    return score


def max_word_value(words=[]):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if len(words) < 1:
        words = load_words()
    word_values = [calc_word_value(w) for w in words]
    mword, _ = max(zip(words, word_values), key=lambda x: x[1])
    return mword


if __name__ == "__main__":
    pass  # run unittests to validate