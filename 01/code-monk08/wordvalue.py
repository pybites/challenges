from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    return open(DICTIONARY).read().splitlines()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char, 0) for char in word.upper())


def max_word_value(list_of_words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return sorted(list_of_words, reverse=True, key=calc_word_value)[0]

