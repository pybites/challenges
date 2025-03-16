import pytest
from multiplication_table import multiplication

# @pytest.mark.xfail()
def test_multiplication(capfd):
    x = [5, 6]
    y = [5, 6]
    multiplication(x, y)
    output = capfd.readouterr()[0].strip()
    assert output == '''5\t 6\n5\t 25\t 30\n6\t 30\t 36'''
