from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        words = file.read().split()
    return words
            

def calc_word_value(words):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for letter in words:
        if letter.upper() in LETTER_SCORES:
            word_value += LETTER_SCORES[letter.upper()]
    return word_value

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max((calc_word_value(word), word) for word in words)[1]