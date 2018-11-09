from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        return [s.strip() for s in f.readlines()]
    return []

def calc_word_value(w):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum((LETTER_SCORES.get(c.upper(),0) for c in w))

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    ms = 0
    mw = ''
    for w in words:
        sc = calc_word_value(w)
        if sc > ms:
            ms = sc
            mw = w
    return mw

if __name__ == "__main__":
    words = load_words()
    print(words[:10])
    print(max_word_value(words))
    pass # run unittests to validate
