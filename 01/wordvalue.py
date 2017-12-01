from data import DICTIONARY, LETTER_SCORES
from functools import reduce

def comp_words(word1, word2):
    if calc_word_value(word1) >= calc_word_value(word2):
        return word1
    else:
        return word2

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        word_list = f.read().split()
    return word_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    word = word.upper()
    for letter in word:
        if letter in LETTER_SCORES:
            value += LETTER_SCORES[letter]
    return value

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words == None:
        words = load_words()
    max_word = reduce(lambda w1, w2: comp_words(w1, w2), words)
    return max_word

if __name__ == "__main__":
    pass # run unittests to validate
