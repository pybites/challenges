from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        wordlist = f.read().splitlines()
    return wordlist

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word:
        value += LETTER_SCORES.get(letter.upper(),0)
    return value

def max_word_value(wordlist=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if wordlist is None:
        wordlist = load_words()
    word_values = {}
    for word in wordlist:
        word_values[word] = calc_word_value(word)
    return max(word_values.iterkeys(), key=(lambda key: word_values[key]))

if __name__ == "__main__":
    pass # run unittests to validate
