import string

from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    f = open(DICTIONARY, 'r')
    dictionary_list = [_.strip() for _ in f.readlines()]
    f.close()
    return dictionary_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[key] for key in word.upper() if key in string.ascii_uppercase)


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return sorted([(_, calc_word_value(_)) for _ in words], key=lambda a: a[1])[-1][0]


if __name__ == "__main__":
    pass  # run unittests to validate
