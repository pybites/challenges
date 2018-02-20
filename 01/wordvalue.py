from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    
    #print("Loading dictionary from file...")

    iFile = open(DICTIONARY, 'r')

    words = []
    
    words = [line.strip() for line in iFile]
    
    #print("  ", len(words), "words loaded.")
    
    return words

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    
    load_words()
