from data import DICTIONARY, LETTER_SCORES
import unittest

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words = f.read().splitlines()
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.isalpha():
            score += LETTER_SCORES[letter.capitalize()]
    return score

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()
    highScore = 0
    bestWord = ''
    for word in words:
        if calc_word_value(word) > highScore:
            highScore = calc_word_value(word)
            bestWord = word
    return bestWord

if __name__ == "__main__":
    import test_wordvalue
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromModule(test_wordvalue))
    unittest.TextTestRunner().run(suite)
