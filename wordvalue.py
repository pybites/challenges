from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    wordlist = []
    with open(DICTIONARY) as file_handler:
        for word in file_handler.readlines():
            wordlist.append(word.rstrip())
    return wordlist

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    val = 0
    for letter in word:
        if letter.isalpha():
            val = val + LETTER_SCORES[letter.upper()]
    return val
            

def max_word_value(wordlist=[]):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    
    if len(wordlist)==0:
        wordlist = load_words()
    max = 0
    max_word = ""

    for word in wordlist:
        val = calc_word_value(word)
        if(val > max):
            max = val
            max_word = word
    return max_word
        

if __name__ == "__main__":
    pass # run unittests to validate
