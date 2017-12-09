from fizzbuzz import check_value, fizzbuzz, fizz_check, fizz_gen
from pytest import raises


def test_check_value():
    """ Tests for invalid values """
    with raises(ValueError):
        check_value(True)
    with raises(ValueError):
        check_value(0)
    with raises(ValueError):
        check_value(-3)
    with raises(ValueError):
        fizz_check('15')
    with raises(ValueError):
        fizz_check(15.4563)
    with raises(TypeError):
        check_value(list())
    with raises(ValueError):
        fizz_check('Hello')


def test_fizz_check():
    """ Tests for valid values """
    assert fizz_check(1) == 1
    assert fizz_check(3) == 'Fizz'
    assert fizz_check(5) == 'Buzz'
    assert fizz_check(15) == 'FizzBuzz'
    assert fizz_check(1287341875) == 'Buzz'


def test_fizz_gen():
    """ Tests for valid generator behavior """
    numbers = fizz_gen(2)
    assert next(numbers) == 1
    assert next(numbers) == 2
    with raises(StopIteration):
        next(numbers)
    word = fizz_gen('World!')
    with raises(ValueError):
        next(word)


def test_fizzbuzz(capsys):
    """ Sample valid test run """
    fizzbuzz(15)
    out, err = capsys.readouterr()
    assert out == ('1\n'
                   '2\n'
                   'Fizz\n'
                   '4\n'
                   'Buzz\n'
                   'Fizz\n'
                   '7\n'
                   '8\n'
                   'Fizz\n'
                   'Buzz\n'
                   '11\n'
                   'Fizz\n'
                   '13\n'
                   '14\n'
                   'FizzBuzz\n')
