from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as fh:
        # DICTIONARY file has one word per line
        return [word.strip() for word in fh]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char, 0) for char in word.upper())


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_value_word = ''

    words = load_words() if not words else words

    for word in words:
        word_value = calc_word_value(word)
        if word_value > max_value:
            max_value_word, max_value = word, word_value

    return max_value_word


if __name__ == "__main__":
    max_word_value  # run unittests to validate
