import re

from data import DICTIONARY, LETTER_SCORES

CHARS_REGEX = re.compile('[a-zA-Z]+')


def load_words() -> list:
    """
    Loads words from the file designated by the DICTIONARY constant into a list
    (trailing newline characters are stripped)
    @return: the words in DICTIONARY as a list
    """
    words: list
    with open(DICTIONARY) as f:
        words = [line.rstrip('\n') for line in f]
    return words


def calc_word_value(word: str) -> int:
    """
    Calculates the scabble value of the word specified
    @param word: the word value to calculate the scabble value for
    @return: the scrabble value (an integer)
    """
    value: int = 0
    for c in ''.join(CHARS_REGEX.findall(word)):
        value += LETTER_SCORES[c.upper()]
    return value


def max_word_value(dictionary: list = None) -> str:
    """
    Determine the word in dictionary which provides the highest scrabble score
    @param dictionary: an optional list of alternate words to check. If not specified, load_words() will be used
    @return: the word in dictionary providing the highest scrabble score
    """
    dictionary = load_words() if dictionary is None else dictionary
    word: str = ''
    value: int = 0
    for check_word in dictionary:
        check_word_value = calc_word_value(check_word)
        if check_word_value > value:
            word = check_word
            value = check_word_value
    return word


if __name__ == "__main__":
    print(max_word_value())
