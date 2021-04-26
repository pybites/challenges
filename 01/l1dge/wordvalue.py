import os, unittest

from data import DICTIONARY, LETTER_SCORES

CWD = "/Users/l1dge/Dev/pybites/challenges/01/l1dge"

DICT = "dictionary.txt"
DICTIONARY = os.path.join(CWD, DICT)


def load_words():
    """Load dictionary into a list and return list"""
    lines = []
    with open(DICTIONARY) as file:
        for line in file:
            line = line.strip()
            lines.append(line)

    return lines


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        letter = letter.upper()
        if letter in LETTER_SCORES:
            score += LETTER_SCORES[letter]

    return score


def max_word_value(words={}):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    my_result = {}

    if words is max_word_value.__defaults__[0]:
        for word in load_words():
            my_result.update({word: calc_word_value(word)})
    else:
        for word in words:
            my_result.update({word: calc_word_value(word)})

    keymax = max(my_result, key=my_result.get)
    # for wrd, value in my_result.items():
    #     if wrd == keymax:
    #         print(f"Highest scoring word is {keymax.upper()} with a value of {value}")

    return keymax


if __name__ == "__main__":
    pass  # run unittests to validate
