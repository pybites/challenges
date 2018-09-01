from data import DICTIONARY, LETTER_SCORES
import functools as ft


def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY, 'r') as input:
        for line in input:
            line = line.strip()
            if line != '':
                words.append(line)
    return words


def calc_word_value(input):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return ft.reduce(lambda x, y: x + LETTER_SCORES.get(y.upper(), 0),
                     input, 0)


def max_word_value(dictionary=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    dictionary = dictionary if dictionary is not None else load_words()
    max_word = ''
    max_value = 0
    for w in dictionary:
        value = calc_word_value(w)
        if value > max_value:
            max_word = w
            max_value = value
            # print(f'new max value found: {max_word} => {max_value}')
    return max_word
