import unittest

from data import DICTIONARY, LETTER_SCORES
from wordvalue import load_words, calc_word_value, max_word_value

WORDS_LIST = ['abdominous', 'accusatorially', 'neocyte', 'devolution', 'transeunt']


class TestWordValues(unittest.TestCase):

    def test_load_words(self):
        words = load_words()
        self.assertEqual(len(words), 235886)
        self.assertEqual(words[0], 'A')
        self.assertEqual(words[-1], 'Zyzzogeton')
        self.assertNotIn(' ', ''.join(words))

    def test_calc_word_value(self):
        self.assertEqual(calc_word_value('abdominous'), 15)
        self.assertEqual(calc_word_value('accusatorially'), 21)
        self.assertEqual(calc_word_value('neocyte'), 12)
        self.assertEqual(calc_word_value('devolution'), 14)
        self.assertEqual(calc_word_value('transeunt'), 9)

    def test_max_word_value(self):
        self.assertEqual(max_word_value(WORDS_LIST), 'accusatorially')
        self.assertEqual(max_word_value(), 'benzalphenylhydrazone')


if __name__ == "__main__":
    unittest.main()
