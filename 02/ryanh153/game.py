#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
from itertools import permutations, islice
import copy

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

# check if user word is valid
def checkValid(word, letters):
	valid = True
	tempLetters = copy.deepcopy(letters)
	for letter in word:
		if letter in tempLetters:
			tempLetters.remove(letter)
		else:
			valid = False
			break

	if word.lower() not in DICTIONARY:
		valid = False

	return valid

# get all possible words from the given list letters
def getBest(letters, maxScore, maxLetters):
	possibleWords = ["".join(word) for word in permutations(letters) if "".join(word).lower() in DICTIONARY]
	if len(possibleWords) > 0:
		currWord = max_word_value(possibleWords)
		currScore = calc_word_value(currWord)
	else:
		currScore = 0

	if currScore > maxScore:
		maxScore = currScore
		maxLetters = currWord

	if len(letters) > 0:
		for i in range(len(letters)):
			if i != len(letters)-1:
				maxLetters, maxScore = getBest(letters[:i]+letters[i+1::], maxScore, maxLetters)
			else:
				maxLetters, maxScore = getBest(letters[:i], maxScore, maxLetters)

	return maxLetters, maxScore


def main():
	random.shuffle(POUCH)
	letters = POUCH[:NUM_LETTERS]
	print("Letters drawn: %s" % (",".join(letters)))

	playerWord = input("Form a valid word: ").upper()
	valid = checkValid(playerWord, letters)

	if valid:
		playerScore = calc_word_value(playerWord)
		print("Word chosen: %s (value: %d)" % (playerWord, playerScore))
	else:
		playerScore = 0
		print("You did not submit a valid word.")

	maxWord, maxScore = getBest(letters, 0, letters) # 0 is initial score, start with just the list

	print("Optimal word possible: %s (value: %d)" % ("".join(maxWord).lower(), maxScore))
	print("You scored: %.1f" % (playerScore/maxScore))



if __name__ == "__main__":
    main()
