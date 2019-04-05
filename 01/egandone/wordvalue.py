from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
      words = [line.strip() for line in f.readlines()]
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[l] for l in word.upper() if l in LETTER_SCORES])

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if (words == None):
      words = load_words()
    max_word = max(words, key=calc_word_value)
    return max_word

if __name__ == "__main__":
    pass # run unittests to validate
