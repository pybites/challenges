from data import DICTIONARY, LETTER_SCORES

def load_words():
    file = open(DICTIONARY, "r")
    return file.read().strip().split("\n")

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word:
        if letter.isalpha():
            value += LETTER_SCORES[letter.upper()]
    return value

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_word =""
    for word in words:
        value = calc_word_value(word)
        if value > max_value:
            max_value = value
            max_word = word
    return max_word

if __name__ == "__main__":
    pass