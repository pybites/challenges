from data import DICTIONARY, LETTER_SCORES


def load_words():
    words = []
    with open(DICTIONARY) as f:
        for line in f:
            words.append(line.strip())

    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[letter] for letter in word.upper() if letter in LETTER_SCORES.keys()])


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scores = {word: calc_word_value(word) for word in words}
    return max(scores, key=scores.get)


if __name__ == "__main__":
    pass  # run unittests to validate
