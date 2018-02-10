from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as fin:
        words = [line.strip() for line in fin]
    return words


def calc_word_value(w):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = list(w.upper())
    counter = 0
    for letter in word:
        counter += LETTER_SCORES.get(letter, 0)
    return counter


def max_word_value(wordlist=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if wordlist is None:
        words = load_words()
    else:
        words = wordlist
    word_value = [(calc_word_value(word), word) for word in words]
    return max(word_value)[1]


if __name__ == "__main__":
    pass  # run unittests to validate
