from data import DICTIONARY, LETTER_SCORES
from typing import Optional, List


def load_words() -> List[str]:
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return [line.strip() for line in f.readlines()]


def calc_word_value(word: str) -> int:
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[letter] for letter in list(word.replace('-', '').upper()))


def max_word_value(dictionary: Optional[List[str]] = None) -> str:
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if dictionary is None:
        dictionary = load_words()
    return max(dictionary, key=calc_word_value)
