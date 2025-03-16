import importlib

from importlib.machinery import SourceFileLoader

import pytest

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


@pytest.mark.parametrize("number", [-1, 1, 16])
def test_fizzbuzz_number(number):
    """The result for these numbers is their string."""
    assert fizzbuzz.fizzbuzz(number) == f"{number}"


@pytest.mark.parametrize("number", [3, -3, 9, -9, 12, -12])
def test_fizzbuzz_fizz(number):
    """The result for these numbers is 'Fizz'."""
    assert fizzbuzz.fizzbuzz(number) == "Fizz"


@pytest.mark.parametrize("number", [5, -5, 20, -20])
def test_fizzbuzz_buzz(number):
    """The result for these numbers is 'Buzz'."""
    assert fizzbuzz.fizzbuzz(number) == "Buzz"


@pytest.mark.parametrize("number", [0, 15, 45, -15, -45])
def test_fizzbuzz_fizzbuzz(number):
    """The result for these numbers is 'FizzBuzz'."""
    assert fizzbuzz.fizzbuzz(number) == "FizzBuzz"


@pytest.mark.parametrize("number", ["", 3.0, 2.5, "2", None])
def test_fizzbuzz_with_value_errors(number):
    """The result for these numbers is a ValueError."""
    with pytest.raises(ValueError):
        fizzbuzz.fizzbuzz(number)


def test_fizzbuzz_100():
    """Check fizzbuzz_100() returns the first 100 fizzbuzz numbers."""
    fizzbuzz.fizzbuzz_100() == FIZZBUZZ_100


def test_fizzbuzz_main(capsys):
    """Check fizzbuzz.main() prints the first 100 fizzbuzz numbers."""
    fizzbuzz.main()
    out, err = capsys.readouterr()
    assert out == FIZZBUZZ_100 + "\n"
    assert err == ''


def test_fizzbuzz_standalone(capsys):
    """Check calling fizzbuzz prints the first 100 fizzbuzz numbers."""
    SourceFileLoader('__main__', 'fizzbuzz.py').load_module()
    out, err = capsys.readouterr()
    assert out == FIZZBUZZ_100 + "\n"
    assert err == ''


def test_fizzbuzz_imported(capsys):
    """Check that nothing is printed when module is imported."""
    importlib.reload(fizzbuzz)
    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''
