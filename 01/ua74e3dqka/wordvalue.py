from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as d_fp:
        return [word.strip() for word in d_fp.readlines()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum(LETTER_SCORES.get(c.upper(), 0) for c in word)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()

    return max(words, key=lambda w: calc_word_value(w)) 
    

if __name__ == "__main__":
    pass # run unittests to validate
