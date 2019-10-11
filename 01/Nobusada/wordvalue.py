from data import DICTIONARY, LETTER_SCORES
from collections import OrderedDict
import unittest
from os import getcwd
from os.path import join


def load_words():
    """Load dictionary into a list and return list"""
    with open(join(getcwd(), '..', DICTIONARY)) as f:
        dictionary = f.read()
    word_list = dictionary.split('\n')
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for i in word:
        if i is not '-':
            value += LETTER_SCORES[i.upper()]
    return value


def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list is None:
        word_list = load_words()
    value_list = [calc_word_value(i) for i in word_list]
    word_value_od = OrderedDict(zip(word_list, value_list))
    reversed_word_value_od = OrderedDict(sorted(word_value_od.items(), reverse=True, key=lambda key: key[1]))
    return reversed_word_value_od.popitem(last=False)[0]


class Tests(unittest.TestCase):
    def test_load_words(self):
        words = load_words()
        self.assertIsInstance(words, list)

    def test_calc_word_value(self):
        self.assertEqual(calc_word_value('AEIDBCFWKJXQQ'), 60)
        self.assertEqual(calc_word_value('aeidbcfwkjxqq'), 60)

    def test_max_word_value_with_list(self):
        word = ['A']
        max_word = max_word_value(word)
        self.assertEqual(calc_word_value(max_word), 1)

    def test_max_word_value_without_list(self):
        # The word with max value is benzalphenylhydrazone with value of 56
        max_word = max_word_value()
        self.assertEqual(calc_word_value(max_word), 56)


if __name__ == "__main__":
    unittest.main()
