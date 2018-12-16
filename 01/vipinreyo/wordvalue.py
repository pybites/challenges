from data import DICTIONARY, LETTER_SCORES
import string


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as df:
        return df.read().split()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[l.upper()] for l in word if l in string.ascii_letters])


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if not words:
        words = load_words()

    word_values = [(word, calc_word_value(word)) for word in words]
    return sorted(word_values, key=lambda x: x[1], reverse=True)[0][0]


if __name__ == "__main__":
    WORDS_LIST = ['abdominous', 'accusatorially', 'neocyte', 'devolution', 'transeunt']
    print(max_word_value())
