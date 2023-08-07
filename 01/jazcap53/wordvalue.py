from data import DICTIONARY, LETTER_SCORES

def load_words(dictionary=DICTIONARY):
    """Load dictionary into a list and return list"""
    with open(dictionary) as words:
        return [w.strip() for w in list(words)]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[letr.upper()] for letr in word if letr.isalpha())

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not word_list:
        word_list = load_words()
    return max(word_list, key=calc_word_value)
