from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words = f.read().splitlines()
    return words

def calc_word_value(words):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    calculated_data = sum(LETTER_SCORES.get(char, 0) for char in words.upper())
    return calculated_data

def max_word_value(list_words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return sorted(list_words, reverse=True, key=calc_word_value)[0]

if __name__ == "__main__":
    pass # run unittests to validate
