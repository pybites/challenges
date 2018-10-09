from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dictionary_file:
        lst = dictionary_file.read().split('\n')[:-1]
    return lst

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for letter in word:
        if LETTER_SCORES.get(letter.upper()):
            word_value += LETTER_SCORES[letter.upper()]
    return word_value

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words:
        return max(words, key=calc_word_value)
    else:
        return max(load_words(), key=calc_word_value)
    

if __name__ == "__main__":
    pass # run unittests to validate
