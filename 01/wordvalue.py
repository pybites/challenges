from data import DICTIONARY, LETTER_SCORES

def load_words():
	"""Load dictionary into a list and return list"""
	with open(DICTIONARY) as f:
		return [word.strip() for word in f.read().split()]
	pass

def calc_word_value(word):
	"""Calculate the value of the word entered into function
	using imported constant mapping LETTER_SCORES"""
	letter_value = 0
	letter_value = (LETTER_SCORES[letter.upper()] for letter in word)
	return sum(letter_value)
	pass

def max_word_value(all_words):
	"""Calculate the word with the max value, can receive a list
	of words as arg, if none provided uses default DICTIONARY"""
	max_word = all_words[0]
	high_score = 0

	for word in all_words:
		if calc_word_value(word) > high_score:
			max_word = word
			high_score = calc_word_value(word)
	
	return max_word, high_score
	pass

if __name__ == "__main__":
	all_words = load_words()
	max_word, high_score = max_word_value(all_words)

	print("The highest Scrabble score is word: " + max_word + ".")
	print("Score: " + high_score)
	pass # run unittests to validate
