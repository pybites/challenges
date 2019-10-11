from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open('./../dictionary.txt') as f:
        words = f.read().splitlines()
        return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.isalpha():
            score += LETTER_SCORES[letter.upper()]
    return score

def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    maxValue = 0
    maxWord = None
    for word in words:
        currentMax = calc_word_value(word)
        if currentMax > maxValue:
            maxValue = currentMax
            maxWord = word
    return maxWord

if __name__ == "__main__":
    pass # run unittests to validate
