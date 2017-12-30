from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as dictionary:
        content = dictionary.readlines()
    return [line.strip() for line in content]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def max_word_value(word_list=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0    
    max_word = ''
    for word in word_list:
        value = calc_word_value(word)
        if max_value < value:
            max_word = word
            max_value = value 
    return max_word 

if __name__ == "__main__":
    pass # run unittests to validate
