import os
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(os.path.join('..', DICTIONARY), 'r') as fin:
        return [x.strip() for x in fin.readlines()]

def calc_word_value(string):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(x, 0) for x in string.upper()])

def max_word_value(list_of_words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if list_of_words==None:
        list_of_words = load_words()
    elif isinstance(list_of_words, str):
        list_of_words = [list_of_words]
    
    return sorted([(calc_word_value(word), word) for word in list_of_words], 
                  key=lambda x: x[0],
                  reverse=True)[0][1]

if __name__ == "__main__":
    pass # run unittests to validate