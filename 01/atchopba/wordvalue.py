# -*- coding: utf-8 -*-

from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    d = []
    f = open(DICTIONARY)
    for line in f:
        d.append(line.strip())
    f.close()
    return d

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    sum_chars = 0
    for char in word:
        if LETTER_SCORES.get(char.upper()) is not None:
            sum_chars += LETTER_SCORES.get(char.upper())
    return sum_chars

def max_word_value(arr_words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    tmp_word = ""
    tmp_word_value = 0
    for word in arr_words:
        if calc_word_value(word) > tmp_word_value:
            tmp_word = word
            tmp_word_value = calc_word_value(word)
    return tmp_word

if __name__ == "__main__":
    pass # run unittests to validate
