import os
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    lines = []
    dict_path = os.path.join(os.path.curdir, 'yoavcaspi', DICTIONARY)
    with open(dict_path, 'r') as f:
        lines = f.read().splitlines()
    return lines

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[c.upper()] if c.isalpha() else 0 for c in word)

def max_word_value(list_words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if list_words is None:
        list_words = load_words()
    max_word = None
    max_val = 0
    for word in list_words:
        cur_val = calc_word_value(word)
        if cur_val > max_val:
            max_val = cur_val
            max_word = word
    return max_word


if __name__ == "__main__":
    pass # run unittests to validate
