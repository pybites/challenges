# -*- coding: utf-8 -*-

from expects import expect, equal, raise_error
from mamba import description, context, it

from fizzbuzz import fizzbuzz

with description('Playing FizzBuzz') as self:
    with context('when passed the value 3'):
        with it('says "Fizz"'):
            expect(fizzbuzz(3)).to(equal('Fizz'))

    with context('when passed a multiple of 3'):
        with it('says "Fizz"'):
            expect(fizzbuzz(9)).to(equal('Fizz'))

    with context('when passed the value 5'):
        with it('says "Buzz"'):
            expect(fizzbuzz(5)).to(equal('Buzz'))

    with context('when passed a multiple of 5'):
        with it('says "Buzz"'):
            expect(fizzbuzz(20)).to(equal('Buzz'))

    with context('when passed a multiple of 3 and 5'):
        with it('says "FizzBuzz"'):
            expect(fizzbuzz(15)).to(equal('FizzBuzz'))

    with context('when passed a value divisible by neither 3 nor 5'):
        with it('says the value back unchanged'):
            expect(fizzbuzz(1)).to(equal(1))
            expect(fizzbuzz(2)).to(equal(2))

    with context('when passed a none whole integer value'):
        with it('screams and raises a ValueError'):
            # Use lambda to overcome deficiency in expects library
            expect(lambda: fizzbuzz(3.14)).to(raise_error(ValueError))

    with context('when pass a none numeric value'):
        with it('screams and raises a ValueError'):
            # Use lambda to overcome deficiency in expects library
            expect(lambda: fizzbuzz('fred')).to(raise_error(ValueError))
