from operator import itemgetter
from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    all_words = []
    with open("dictionary.txt", "r") as _worddict:
        [all_words.append(word.strip("\n")) for word in _worddict.readlines()]
    return all_words


def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[x.upper()] for x in word if x.upper() in LETTER_SCORES])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()

    word_points_dict = {word: calc_word_value(word) for word in words}
    return max(word_points_dict.items(), key=itemgetter(1))[0]


if __name__ == "__main__":
    pass # run unittests to validate
