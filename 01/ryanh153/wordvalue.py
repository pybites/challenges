from data import DICTIONARY, LETTER_SCORES

"""Load dictionary into a list and return list"""
def load_words():

    with open(DICTIONARY,'r') as dicFile:
        dictionary = dicFile.readlines()

    dictionary = [word.strip() for word in dictionary]

    return dictionary


"""Calculate the value of the word entered into function
using imported constant mapping LETTER_SCORES"""
def calc_word_value(word):
    return sum([LETTER_SCORES[char] for char in word.upper() if char in LETTER_SCORES.keys()])


"""Calculate the word with the max value, can receive a list
of words as arg, if none provided uses default DICTIONARY"""
def max_word_value(words=None):
    if words == None:
        words = load_words()

    scores = [calc_word_value(word) for word in words]

    return words[scores.index(max(scores))]

if __name__ == "__main__":
    pass # run unittests to validate
