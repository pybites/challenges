import unittest
from wordvalue import load_words, calc_word_value, max_word_value
from data import DICTIONARY, LETTER_SCORES
custom_names = ('unittest', 'is', 'good', 'PyTest', 'is', 'Better')


class TestWordValue(unittest.TestCase):

    def test_load_words(self):
        words = load_words()
        self.assertEqual(len(words), 235886)
        self.assertEqual(words[0], 'A')
        self.assertEqual(words[-1], 'Zyzzogeton')
        self.assertEqual(words[118910], 'monoplasmatic')
        self.assertNotIn(' ', ''.join(words))

    def test_calc_word_value(self):
        self.assertEqual(calc_word_value(custom_names[0]), 8)
        self.assertEqual(calc_word_value(custom_names[1]), 2)
        self.assertEqual(calc_word_value(custom_names[2]), 6)
        self.assertEqual(calc_word_value(custom_names[3]), 11)
        self.assertEqual(calc_word_value(custom_names[4]), 2)
        self.assertEqual(calc_word_value(custom_names[5]), 8)

    def test_max_word_value(self):
        words = load_words()
        self.assertEqual(max_word_value(words), 'benzalphenylhydrazone')
        self.assertEqual(max_word_value(custom_names), 'PyTest')


if __name__ == '__main__':
    unittest.main()

