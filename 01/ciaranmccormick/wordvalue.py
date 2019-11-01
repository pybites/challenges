from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    pass
    with open(DICTIONARY, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    return lines


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(l.upper(), 0) for l in word])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    m = max([(word, calc_word_value(word)) for word in words], key=lambda x: x[1])
    return m[0]


if __name__ == "__main__":
    pass  # run unittests to valid
