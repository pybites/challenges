from data import LETTER_SCORES, DICTIONARY 
import os

#File path for Dictionary
fname = os.path.join('../',DICTIONARY)

#Wordlist from dictionary
def load_words() -> list:
    with open(fname,'r') as f:
        wordlist = f.read().split()
        return wordlist

def calc_word_value(word:str) -> int:
    score = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES:
            score += LETTER_SCORES[letter.upper()]
    return score

def max_word_value(words=None):
    wordvalue_pair = list()
    #checking if given argument
    if words == None:
        wordlist = load_words()
    else:
        wordlist = words
    for word in wordlist:
        score = calc_word_value(word)
        wordvalue_pair.append( (word,score) )
    result = max(wordvalue_pair, key=lambda x: x[1])
    return result[0]


