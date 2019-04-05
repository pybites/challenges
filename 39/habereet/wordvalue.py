from data import scrabble_scores, LETTER_SCORES

def get_data_file():
	return "dictionary.txt"

def read_dictionary():
	with open(get_data_file()) as file:
		lines = file.readlines()

	lines = [line.strip() for line in lines] 

	return lines

def word_value(word):
	word_score = 0
	for character in word:
		if character.isalpha():
			word_score += letter_value(character.upper())
	return word_score
		
def letter_value(letter):
	return LETTER_SCORES[letter]
	
def calculate_max_word(current_max, test):
	if test[1] > current_max[1]:
		return test
	else:
		return current_max

def find_max_word():
	max_word = ("", 0)
	words = read_dictionary()
	for word in words:
		test=(word, word_value(word))
		max_word = (calculate_max_word(max_word, test))
	return max_word

if __name__ == "__main__":
	max_word = find_max_word()
	print(f'The word in {get_data_file()} with the largest Scrabble value is {max_word[0]} with a value of {str(max_word[1])}.')