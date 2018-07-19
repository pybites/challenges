from data import scrabble_scores, LETTER_SCORES

def read_dictionary():
	with open("dictionary.txt") as file:
		words = file.readlines()

	words = [word.strip() for word in words] 

	return words

def word_value(word):
	for letter in word:
		print(letter)

if __name__ == "__main__":
	words = read_dictionary()
	word_value(words[3])