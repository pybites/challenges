from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = list()
    with open(DICTIONARY) as fd:
        for line in fd:
            words.append(line.rstrip('\n'))
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for char in word:
        char = char.upper()
        if char in LETTER_SCORES:
            value += LETTER_SCORES[char]
    return value

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = None
    max_value = 0

    if not words:
        words = load_words()

    for word in words:
        value = calc_word_value(word)
        if value > max_value:
            max_word = word
            max_value = value
    return max_word

if __name__ == "__main__":
    pass # run unittests to validate

