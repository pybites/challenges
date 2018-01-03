import re

from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = DICTIONARY.split('\n')
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_list = list(re.sub(r'-', '', word))
    word_value = [LETTER_SCORES[char.upper()] for char in word_list]
    return sum(word_value)


def max_word_value(word_list):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(word_list)

if __name__ == "__main__":
    words = load_words()
    word_values = []
    for word in words:
        word_values.append(calc_word_value(word))
    print(max_word_value(word_values))
