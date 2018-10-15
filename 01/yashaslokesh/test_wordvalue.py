import pytest

from data import DICTIONARY, LETTER_SCORES
from wordvalue import load_words, calc_word_value, max_word_value

WORDS = ["Vikas","Oxygen","Buckminsterfullerene"]

def test_load_words():
    words_dict = load_words()
    assert words_dict[0] == "A"
    assert words_dict[119637] == "morphogenetic"
    assert len(words_dict) == 235886

def test_calc_word_value():
    assert calc_word_value(WORDS[0]) == 12
    assert calc_word_value(WORDS[1]) == 17
    assert calc_word_value(WORDS[2]) == 33

def test_max_word_value():
    assert max_word_value() == "benzalphenylhydrazone"
    assert max_word_value(WORDS) == "Buckminsterfullerene"





