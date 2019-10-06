import re

from data import DICTIONARY, LETTER_SCORES

char = re.compile(r"[A-Z]{1}")  # I want to match individual UPPER CASE LETTERS


def load_words() -> list:
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, "r") as words:
        return words.read().splitlines()


def calc_word_value(word: str) -> int:
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[c] for c in char.findall(word.upper()))


def max_word_value(list_of_words: list = None) -> str:
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if list_of_words is None:
        list_of_words = load_words()
    else:
        list_of_words = list(list_of_words)

    list_of_words.sort(key=calc_word_value, reverse=True)

    return list_of_words[0]


if __name__ == "__main__":
    pass  # run unittests to validate
