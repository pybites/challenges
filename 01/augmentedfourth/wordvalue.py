from data import DICTIONARY, LETTER_SCORES
import types

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return [word.strip() for word in f.read().split()]
    #wordlist = []
    #if isinstance(openfile, (tuple, list)):
    #    for element in openfile:
    #        wordlist.append(element.strip())
    #else:
    #    with open(openfile) as file:
    #        for line in file:
    #            wordlist.append(line.strip())
    #return wordlist

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)
    #value = 0
    #for letter in word:
    #    if letter.upper() in LETTER_SCORES:
    #        value = value + LETTER_SCORES[letter.upper()]
    #return value

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    #highword = ["",0]
    #for word in words:
    #    currentword = [word, calc_word_value(word)]
    #    if currentword[1] > highword[1]:
    #        highword = currentword
    #return highword[0]
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass
