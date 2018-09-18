#! /usr/bin/env python3
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY, 'r' ) as f:
        words = []
        for word in f:
            words.append(word[:-1])
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    value = 0
    for letter in word:
        if type(LETTER_SCORES.get(letter[0].upper())) != type(None):
            value = value + int(LETTER_SCORES.get(letter[0].upper()))
    return value

def max_word_value(words=open(DICTIONARY, 'r' )):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    best_value = 0
    value = 0
    best_word = ''
    for word in words:
        value = calc_word_value(word)
        if best_value < value:
            best_value = value
            best_word = word
    if best_word[-1] == '\n':
        return best_word[:-1]
    else: 
        return best_word

if __name__ == "__main__":

    #print(max_word_value())
    pass
