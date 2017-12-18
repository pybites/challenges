import pytest
from fizzy import fizzbuzz



@pytest.mark.parametrize("given_input, expected_output",[
	(1, 1),
	(3, 'fizz'),
	(5, 'buzz'),
	(15, 'fizzbuzz'),
	(11, 11)])
def test_fizzbuzz(given_input, expected_output):

	assert fizzbuzz(given_input) == expected_output
	




