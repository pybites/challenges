
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY,'r') as f:
        list_words=f.read().split()
    return list_words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value=0
    for letter in word:
        if letter.isalpha():
            value+=LETTER_SCORES[letter.upper()]
    return value

def max_word_value(list_words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    dict_values={}
    for word in list_words:
        dict_values[word]=calc_word_value(word)
    return max(dict_values, key=lambda key: dict_values[key])

if __name__ == "__main__":
    print(max_word_value()) # run unittests to validate

