import pytest
from fizzbuzz import fizzbuzz, display_fizzbuzz


def test_invalid_input_fizzbuzz():
    """Tests fizzbuzz handling of invalid input"""
    with pytest.raises(ValueError):
        fizzbuzz('FAIL')
    with pytest.raises(ValueError):
        fizzbuzz(3.5)


def test_invalid_input_display_fizzbuzz():
    """Tests display_fizzbuzz handling of invalid input"""
    with pytest.raises(ValueError):
        display_fizzbuzz('FAIL')
    with pytest.raises(ValueError):
        display_fizzbuzz(3.5)


def test_fizz():
    """Tests if fizzbuzz returns Fizz for multiples of 3"""
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(9) == 'Fizz'
    assert fizzbuzz(63) == 'Fizz'


def test_buzz():
    """Tests if fizzbuzz returns Buzz for multiples of 5"""
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(55) == 'Buzz'


def test_fizzbuzz():
    """Tests if fizzbuzz returns FizzBuzz for multiples of 3 and 5"""
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(30) == 'FizzBuzz'
    assert fizzbuzz(90) == 'FizzBuzz'


def test_nofizznobuzz():
    """Tests if fizzbuzz returns a number for non-multiples of 3 and/or 5"""
    assert fizzbuzz(1) == 1
    assert fizzbuzz(7) == 7
    assert fizzbuzz(92) == 92


def test_print_fizz(capsys):
    """Tests if display_fizzbuzz prints Fizz correctly to stdout"""
    display_fizzbuzz(3)
    out, err = capsys.readouterr()
    assert out == "Fizz\n"
    display_fizzbuzz(9)
    out, err = capsys.readouterr()
    assert out == "Fizz\n"
    display_fizzbuzz(33)
    out, err = capsys.readouterr()
    assert out == "Fizz\n"


def test_print_buzz(capsys):
    """Tests if display_fizzbuzz prints Buzz correctly to stdout"""
    display_fizzbuzz(5)
    out, err = capsys.readouterr()
    assert out == "Buzz\n"
    display_fizzbuzz(10)
    out, err = capsys.readouterr()
    assert out == "Buzz\n"
    display_fizzbuzz(55)
    out, err = capsys.readouterr()
    assert out == "Buzz\n"


def test_print_fizzbuzz(capsys):
    """Tests if display_fizzbuzz prints FizzBuzz correctly to stdout"""
    display_fizzbuzz(15)
    out, err = capsys.readouterr()
    assert out == "FizzBuzz\n"
    display_fizzbuzz(30)
    out, err = capsys.readouterr()
    assert out == "FizzBuzz\n"
    display_fizzbuzz(60)
    out, err = capsys.readouterr()
    assert out == "FizzBuzz\n"


def test_print_nofizznobuzz(capsys):
    """Tests if display_fizzbuzz prints non-multiples correctly to stdout"""
    display_fizzbuzz(4)
    out, err = capsys.readouterr()
    assert out == "4\n"
    display_fizzbuzz(11)
    out, err = capsys.readouterr()
    assert out == "11\n"
    display_fizzbuzz(98)
    out, err = capsys.readouterr()
    assert out == "98\n"
