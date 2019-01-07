from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as fin:
        x = fin.read().splitlines()
    return x

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    x = sum([LETTER_SCORES.get(char.upper(), 0) for char in word])
    return x

def max_word_value(text=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if text is None:
        x = load_words()
        wordScores = [sum([LETTER_SCORES.get(char.upper(), 0) for char in i]) for i in x]
        d = dict(zip(x, wordScores))
        maximum = max(d, key=d.get)
        return maximum
    else:

        wordScores = [sum([LETTER_SCORES.get(char.upper(), 0) for char in i]) for i in text]
        d = dict(zip(text, wordScores))
        maximum = max(d, key=d.get)
        return maximum

if __name__ == "__main__":
    load_words()
    calc_word_value()
    max_word_value()
    #pass # run unittests to validate