from sys import exit
from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    try:
        with open(DICTIONARY, 'r') as d:
            return [word.rstrip() for word in d.readlines()]
    except IOError as e:
        print('The dictionary file "{}" was not found.'.format(e.filename))
        exit()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[l.upper()] for l in word if l.isalpha()])


def max_word_value(words=[]):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    words = load_words() if len(words) == 0 else words

    # method 1
    max_value = ('', 0)

    for word in words:
        val = calc_word_value(word)
        max_value = (word, val) if val > max_value[1] else max_value
    return max_value[0]

    # method 2 (too slow)
    # word_values = {}
    # for word in words:
    #     word_values[word] = calc_word_value(word)
    # return max(word_values, key=word_values.get)

    # method 3 (way too slow)
    # word_values = dict(zip(words, [calc_word_value(word) for word in words]))
    # return max(word_values, key=word_values.get)


if __name__ == "__main__":
    pass # run unittests to validate
