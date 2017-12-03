from data import LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open('dictionary.txt','r') as f:
        lines = f.read().splitlines()
    return lines


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for letter in word:
        word_value += LETTER_SCORES.get(letter.upper(), 0)
    return word_value


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max((calc_word_value(word), word) for word in words)[1]


if __name__ == "__main__":
    pass  # run unittests to validate
