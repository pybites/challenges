from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dic:
       return [l.strip() for l in dic] 

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pts = sum([LETTER_SCORES[l.upper()] for l in word if l.upper() in LETTER_SCORES]) 
    return pts

def max_word_value(list_of_words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scores = map(calc_word_value, list_of_words)
    return list_of_words[scores.index(max(scores))] 

if __name__ == "__main__":  
    pass
