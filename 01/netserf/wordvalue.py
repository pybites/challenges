from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        lines = file.read().splitlines()
    return lines

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = (None, 0)  # (word, word_value) tuple
    for word in words:
        value = calc_word_value(word)
        if value > max_word[1]:
            max_word = (word, value)
    return max_word[0]

if __name__ == "__main__":
    pass # run unittests to validate
