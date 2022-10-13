from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words = f.read().splitlines()
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[c.upper()] for c in word if c.isalpha()])


def max_word_value(lst=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    lst = lst or load_words()
    return max(lst, key=calc_word_value)


if __name__ == "__main__":
    pass # run unittests to validate
