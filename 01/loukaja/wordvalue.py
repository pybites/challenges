from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return (f.read().split())

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for char in word:
        if char.isalpha():
            value += LETTER_SCORES[char.upper()]
    
    return value

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list is None:
        word_list = load_words()

    max_value = 0
    max_word = ''

    for word in word_list:
        if len(word) * 10 < max_value:
            continue # no point in calculating if the value can't reach above current max
        value = calc_word_value(word)
        if value > max_value:
            max_word = word
            max_value = value
    
    return max_word

if __name__ == "__main__":
    pass # run unittests to validate
