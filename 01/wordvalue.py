from data import DICTIONARY, LETTER_SCORES
import string

def load_words():
    """Load dictionary into a list and return list"""
    
    #print("Loading dictionary from file...")

    iFile = open(DICTIONARY, 'r')

    words = []
    
    words = [line.strip() for line in iFile]
    
    #print("  ", len(words), "words loaded.")
    
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    score = 0

    for letter in word:
        if letter not in string.punctuation:
            score += LETTER_SCORES[letter.upper()]
    
    return score

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    
    max_value = 0
    result = None
    
    if words == None:
        words = load_words()
    
    for word in words:
        new_value = calc_word_value(word)
        if new_value > max_value:
            max_value = new_value
            result = word
            
    
    return result

if __name__ == "__main__":
    
    load_words()
