from data import LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open("dictionary.txt", 'r') as dict:
        words = [word.strip("\n") for word in dict.readlines()]
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(x, 0) for x in word.upper()])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    word_values = {calc_word_value(word): word for word in words}
    return word_values.get(max(word_values.keys()))


if __name__ == "__main__":
    pass  # run unittests to validate
