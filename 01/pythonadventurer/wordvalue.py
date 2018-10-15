from data import DICTIONARY, LETTER_SCORES
import pdb

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as d:
        words = [word for word in d.read().split() if word != '']
    
    return words

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[letter.upper()] for letter in word if letter.upper() in ascii_uppercase])

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_values = [calc_word_value(word) for word in words]

    return words[word_values.index(max(word_values))]

if __name__ == "__main__":
    pass # run unittests to validate
