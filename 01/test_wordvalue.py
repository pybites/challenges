import unittest

from data import DICTIONARY, LETTER_SCORES
from wordvalue import load_words, calc_word_value, max_word_value

TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

class TestWordValue(unittest.TestCase):
    
    def setUp(self):
        self.words = load_words()

    def test_load_words(self):
        self.assertEqual(len(self.words), 235886)
        self.assertEqual(self.words[0], 'A')
        self.assertEqual(self.words[-1], 'Zyzzogeton')
        self.assertNotIn(' ', ''.join(self.words))

    def test_calc_word_value(self):
        self.assertEqual(calc_word_value('bob'), 7)
        self.assertEqual(calc_word_value('JuliaN'), 13)
        self.assertEqual(calc_word_value('PyBites'), 14)
        self.assertEqual(calc_word_value('benzalphenylhydrazone'), 56)

    def test_max_word_value(self):
        self.assertEqual(max_word_value(TEST_WORDS), 'barbeque')
        self.assertEqual(max_word_value(), 'benzalphenylhydrazone')

if __name__ == "__main__":
   unittest.main() 
