#!/usr/bin/env python3

import unittest

from wordvalue import load_words, calc_word_value, max_word_value


class TestWordValue(unittest.TestCase):

    def test_load_words(self):
        words = load_words()
        self.assertTrue(len(words) > 0)
        self.assertEqual(words[0], 'A')

    def test_calc_word_value(self):
        self.assertEqual(calc_word_value('fun'), 6)
        self.assertEqual(calc_word_value('apple'), 9)

    def test_max_word_value(self):
        self.assertEqual(max_word_value(['fun', 'apple']), 'apple')
        self.assertEqual(max_word_value(), 'benzalphenylhydrazone')


if __name__ == "__main__":
    unittest.main()
