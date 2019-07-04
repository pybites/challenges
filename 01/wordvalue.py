from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        words = file.read().strip().split('\n')
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for c in word:
        if LETTER_SCORES.get(c.upper()):
            score += LETTER_SCORES.get(c.upper())
    return score


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
        of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    max_score = 0
    max_word = ''
    for w in words:
        t = calc_word_value(w)
        if t > max_score:
            max_score = t
            max_word = w
    return max_word
