from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open('dictionary.txt', 'rb') as f:
        words = [x.replace('\n','') for x in f.readlines()]
    return words

def calc_word_value(word):
    total = []
    for letter in word:
        total.append(LETTER_SCORES.get(letter.upper(), 0))
    return sum(total)
 
def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max((calc_word_value(word), word) for word in words)[1]
 
if __name__ == "__main__":
    pass # run unittests to validate 