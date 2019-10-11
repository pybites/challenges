from data import DICTIONARY, LETTER_SCORES
import os

def load_words(path = DICTIONARY):
    """Load dictionary into a list and return list"""
	fdata=[]
    with open(path) as f:
		rdata = f.read()
		fdata = rdata.splitlines()
	return fdata
	

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
	for s in word:
		score+=LETTER_SCORES[s.upper()]
	return score

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate
