from data import DICTIONARY, LETTER_SCORES

def load_words():
	"""Load dictionary into a list and return list"""
	with open(DICTIONARY) as f:
		all_words = f.read().split()
		return words in all_words
	pass

def calc_word_value():
	"""Calculate the value of the word entered into function
	using imported constant mapping LETTER_SCORES"""
	
	pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
	all_words = load_words()
	for word in all_words:
	calc_word_value()
	
    pass # run unittests to validate
