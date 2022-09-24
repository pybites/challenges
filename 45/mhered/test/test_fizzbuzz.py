#!/usr/bin/python3

import unittest

from app.fizzbuzz import fizzbuzz


class TddFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_returns_ints(self):
        samples = [1, 2, 4, 6, 7, 8, 11, 13]
        for sample in samples:
            result = fizzbuzz(sample)
        self.assertEqual(result, sample)

    def test_fizzbuzz_returns_fizz_with_multiples_of_3(self):
        samples = [3, 6, 9, 12]
        for sample in samples:
            result = fizzbuzz(sample)
        self.assertEqual(result, "Fizz")

    def test_fizzbuzz_returns_buzz_with_multiples_of_5(self):
        samples = [5, 10, 20, 25]
        for sample in samples:
            result = fizzbuzz(sample)
        self.assertEqual(result, "Buzz")

    def test_fizzbuzz_returns_fizzbuzz_with_multiples_of_3_and_5(self):
        samples = [15, 30, 45, 60]
        for sample in samples:
            result = fizzbuzz(sample)
        self.assertEqual(result, "FizzBuzz")

    def test_fizzbuzz_raises_error_message_if_arg_not_int(self):
        self.assertRaises(ValueError, fizzbuzz, 'two')


if __name__ == '__main__':
    unittest.main()
