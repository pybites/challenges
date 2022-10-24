#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random

from itertools import permutations

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Get random letters from the pot"""
    return random.sample(POUCH, NUM_LETTERS)


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    all_options = []

    all_options = _get_permutations_draw(draw)

    dictionary_words = []
    for word in all_options:
        if word.lower() in DICTIONARY:
            dictionary_words.append(word)
    return dictionary_words
    # best_word = max_word_value(dictionary_words)
    # score = calc_word_value(best_word)
    # print(score)


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    for num_letters in range(1, len(draw) + 1):
        for perm in permutations(draw, num_letters):
            yield "".join(perm)


def _isValid(word, draw):

    if len(word) == 0:
        raise ValueError("Couldn't get a word? Want to quit? If you do press y")
    elif len(word) > 7:
        raise ValueError("You need to use the letters shown")

    for letter in word:
        if letter in draw:
            draw.remove(letter)
        else:
            raise ValueError("You need to use the letters shown")

    if word.lower() not in DICTIONARY:
        raise ValueError("Word not in the dictionary")


def main():
    draw = draw_letters()

    get_possible_dict_words(draw)

    print(draw)
    word = input("Enter your word\n").upper()
    _isValid(word, draw)
    score = calc_word_value(word)
    print(score)


if __name__ == "__main__":
    main()
