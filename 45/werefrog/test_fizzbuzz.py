import builtins
import unittest

from unittest.mock import patch

import fizzbuzz


FIZZBUZZ_100 = (
    "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, "
    "FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, "
    "Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, 37, 38, "
    "Fizz, Buzz, 41, Fizz, 43, 44, FizzBuzz, 46, 47, Fizz, 49, Buzz, "
    "Fizz, 52, 53, Fizz, Buzz, 56, Fizz, 58, 59, FizzBuzz, 61, 62, "
    "Fizz, 64, Buzz, Fizz, 67, 68, Fizz, Buzz, 71, Fizz, 73, 74, "
    "FizzBuzz, 76, 77, Fizz, 79, Buzz, Fizz, 82, 83, Fizz, Buzz, 86, "
    "Fizz, 88, 89, FizzBuzz, 91, 92, Fizz, 94, Buzz, Fizz, 97, 98, "
    "Fizz, Buzz")


fizzbuzz.print = lambda *args, **kwargs: builtins.print(*args, **kwargs)


class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(0), "FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(-1), "-1")
        self.assertEqual(fizzbuzz.fizzbuzz(1), "1")

        self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(-3), "Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(-5), "Buzz")

        self.assertEqual(fizzbuzz.fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(20), "Buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(-9), "Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(-20), "Buzz")

        self.assertEqual(fizzbuzz.fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(45), "FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(-15), "FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(-45), "FizzBuzz")

    def test_fizzbuzz_with_value_errors(self):
        self.assertRaises(ValueError, fizzbuzz.fizzbuzz, "")
        self.assertRaises(ValueError, fizzbuzz.fizzbuzz, 3.0)
        self.assertRaises(ValueError, fizzbuzz.fizzbuzz, 2.5)
        self.assertRaises(ValueError, fizzbuzz.fizzbuzz, "2")
        self.assertRaises(ValueError, fizzbuzz.fizzbuzz, None)

    def test_fizzbuzz_100(self):
        self.assertEqual(fizzbuzz.fizzbuzz_100(), FIZZBUZZ_100)

    @patch('builtins.print', autospec=True)
    def test_main(self, mocked_print):
        fizzbuzz.main()
        mocked_print.assert_called_with(FIZZBUZZ_100)


if __name__ == '__main__':
    unittest.main()
