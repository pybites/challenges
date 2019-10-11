from functools import reduce

from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dict_fp:
        return dict_fp.readlines()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return reduce(
        lambda total, char: total+LETTER_SCORES.get(char, 0), word, 0
    )

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    max_value, word = 0, ''

    for curr_word in load_words():
        curr_word_value = calc_word_value(
            curr_word.strip().replace('\n', '').upper()
        )

        if curr_word_value > max_value:
            max_value, word = curr_word_value, curr_word

    return word

if __name__ == "__main__":
    print(max_word_value())
