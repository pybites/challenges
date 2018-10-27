#!/usr/bin/env python3

from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        return [line.rstrip('\n') for line in file]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        score += LETTER_SCORES.get(letter.upper(), 0)

    return score


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_score = 0
    max_word = ''
    for word in words:
        score = calc_word_value(word)
        if score > max_score:
            max_score = score
            max_word = word

    return max_word


if __name__ == "__main__":
    pass  # run unittests to validate
