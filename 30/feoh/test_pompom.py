import pytest
import pompom

def test_decide_break_time():
    assert pompom.decide_break_time(2, 5, 15) == 5
    assert pompom.decide_break_time(5, 5, 15) == 5
    assert pompom.decide_break_time(8, 5, 15) == 15
    assert pompom.decide_break_time(0, 0, 0) == 0
    assert pompom.decide_break_time(-5, 5, 15) == 0
