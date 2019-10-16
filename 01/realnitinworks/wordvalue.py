from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return [
            line.strip()
            for line in f
        ]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum(
        LETTER_SCORES.get(letter, 0)
        for letter in word.upper()
    )


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()

    word_values = {
        word: calc_word_value(word)
        for word in words
    }

    return max(word_values, key=word_values.get)


if __name__ == "__main__":
    print(max_word_value())  # run unittests to validate

