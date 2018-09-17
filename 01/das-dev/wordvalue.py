from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY, 'r') as f:
        return f.read().split()

def calc_word_value(word):
    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)

def max_word_value(dictonary=None):
    return max(dictonary or load_words(), key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
