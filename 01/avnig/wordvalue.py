from data import DICTIONARY, LETTER_SCORES
import unittest


def load_words():
    """Load dictionary into a list and return list"""
    list_of_words = []
    with open(DICTIONARY, 'r') as file:
        list_of_words = [line.strip() for line in file]
    return list_of_words

    # other approache to implement this
    # words = []
    # with open(DICTIONARY, 'r') as f:
    #     for line in f:
    #         line = line.strip()
    #         words.append(line)
    # return words


def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total_score = 0
    for character in word:
        if character.upper() not in LETTER_SCORES:
            continue
        else:
            total_score += LETTER_SCORES[character.upper()]
    return total_score

    # Another way of doing this using comprehension
    # return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    values = {word: calc_word_value(word) for word in words}
    return max(values.keys(), key=(lambda word: values[word]))


if __name__ == "__main__":
    pass
