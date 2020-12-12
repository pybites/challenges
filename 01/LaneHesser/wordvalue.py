from string import ascii_uppercase

from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY) as f:
        return [
            word.strip()
            for word in f.read().split()
        ]


def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    value = 0

    for letter in word:
        letter = letter.upper()
        if letter in ascii_uppercase:
            value += LETTER_SCORES[letter]

    return value

    # return sum([
    #     LETTER_SCORES[letter.upper()]
    #     for letter in word
    # ])


def max_word_value(list_of_words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    biggest, biggest_word = 0, None

    for word in list_of_words:
        current_val = calc_word_value(word)
        if current_val > biggest:
            biggest = current_val
            biggest_word = word

    return biggest_word


    # return max([
    #     calc_word_value(word)
    #     for word in list_of_words
    # ])


if __name__ == "__main__":
    pass
