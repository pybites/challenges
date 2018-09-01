from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
    	return [word.strip() for word in file.read().split()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    #for letter in word:
    #return sum(LETTER_SCORES[letter.upper()])
    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)

	
def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
    	words = load_words()
    	return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate


