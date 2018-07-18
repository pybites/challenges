from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY) as f:
        for line in f:
            words.append(line.strip())
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word:
        value += LETTER_SCORES.get(letter.upper(), 0)
    return value

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()
    values = map(calc_word_value, words)
    lst = list(values)
    maxval = max(lst)
    maxind = lst.index(maxval)
    return words[maxind]

if __name__ == "__main__":
    words = load_words() # run unittests to validate
    print(max_word_value(words))
