from data import DICTIONARY, LETTER_SCORES
import unittest

def load_words(input):
	with open(input, 'r') as f:
		lines = f.readlines()
	return [line.rstrip('\n') for line in lines]

def calc_word_value(input):
	return sum([LETTER_SCORES[letter.upper()] for letter in input 
		if letter.upper() in LETTER_SCORES])

def max_word_value(lst=DICTIONARY):
	if type(lst) != list:
		lst = load_words(lst)
	scores = list(zip(lst, [calc_word_value(word) for word in lst]))
	return max(scores, key=lambda x:x[1])[0]

class TestWordValue(unittest.TestCase):

	def test_calc_word_value(self):
		self.assertEqual(calc_word_value("rabbit"), 10)
		self.assertEqual(calc_word_value("myxomatosis"), 25)
		
	def test_max_word_value(self):
		self.assertEqual(max_word_value(), "benzalphenylhydrazone")
		self.assertEqual(max_word_value(["rabbit", "fox", "badger"]), "fox")
	
if __name__ == "__main__":
	unittest.main()