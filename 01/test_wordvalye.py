import pytest
from wordvalue import load_words, calc_word_value,max_word_value
import data


def test_load_words():
    word_count = load_words()
    assert len(word_count) == 235886
    assert word_count[0] == 'A'

def test_calc_word_value():
    assert calc_word_value('dad') == 5
    assert calc_word_value('A') == 1

def test_max_word_value():
    word_list = ['karim','a','b']
    assert max_word_value(word_list) == 'karim'