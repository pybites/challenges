from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    dl = []
    with open(DICTIONARY) as f:
        for line in f:
            dl.append(line.strip())
    return dl

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for l in word:
        l = l.upper()
        score += LETTER_SCORES.get(l, 0)
    return score


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_val = 0
    max_val_word = None
    if words is None:
        words = load_words()
    for w in words:
        val = calc_word_value(w)
        if val > max_val:
            max_val_word = w
            max_val = val
    return max_val_word



if __name__ == "__main__":
    pass # run unittests to validate

