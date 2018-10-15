from mock import patch
import pytest
import wordvalue
from wordvalue import read_dictionary, word_value, calculate_max_word, letter_value, get_data_file, find_max_word

def test_get_data_file():
	assert get_data_file() == "dictionary.txt"

@patch.object(wordvalue, 'get_data_file')
def test_read_dictionary(get_data_file):
	get_data_file.return_value = "dictionary1.txt"
	assert len(read_dictionary()) == 200


@pytest.mark.parametrize("word, score", [
	('some', 6),
	('beauty', 11),
	('yellow', 12),
	('rude', 5),
	('argues', 7)
])
def test_word_value(word, score):
	assert word_value(word) == score


@pytest.mark.parametrize("letter, score", [
	('D',2),
	('G',2),
	('B',3),
	('C',3),
	('M',3),
	('P',3),
	('F',4),
	('H',4),
	('V',4),
	('W',4),
	('Y',4),
	('K',5),
	('J',8),
	('X',8),
	('Q',10),
	('Z',10),
	('A',1),
	('O',1),
	('I',1),
	('N',1),
	('R',1),
	('T',1),
	('L',1),
	('S',1),
	('U',1)
])
def test_letter_value(letter, score):
	assert letter_value(letter) == score

@patch.object(wordvalue, 'get_data_file')
def find_max_word(get_data_file):
	get_data_file.return_value = "dictionary1.txt"
	assert find_max_word()[0] == 'abdominohysterectomy'


def test_calc_max_score():
	assert calculate_max_word(("a",1),("b",3)) == ("b",3)
	assert calculate_max_word(("c",3),("d",1)) == ("c",3)
	assert calculate_max_word(("e",2),("f",2)) == ("e",2)