#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

# E X A M P L E
# Letters drawn: G, A, R, Y, T, E, V
# Form a valid word: gary  << user input
# Word chosen: GARY (value: 8)
# Optimal word possible: GARVEY (value: 13)
# You scored: 61.5

import itertools

from data import DICTIONARY, LETTER_SCORES, POUCH
from random import choice

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters():
    return [choice(POUCH) for _ in range(7)]


def _validation(word, draw):
    """Validate if letters are in the pouch and if word is in DICTIONARY"""
    for letter in word:
        if letter.upper() not in draw:
            raise ValueError("{} is not in the draw".format(letter.upper()))

    if word not in DICTIONARY:
        raise ValueError("{} is not in the DICTIONARY")


def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    return [w for w in _get_permutations_draw(draw) if w.lower() in DICTIONARY]


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    return [''.join(w).upper()
            for r in range(1, len(draw) + 1)
            for w in itertools.permutations(draw, r)
            ]


def main():
    while True:
        draw = draw_letters()
        print("Letters drawn: %s" % draw)
        guess = input("Form a valid word: ")

        if not _validation(guess, draw):
            continue
        else:
            break

    word_score = calc_word_value(guess)
    print("Word chosen: %s (value: %d)" %
          (guess.upper(), word_score))

    possible_words = get_possible_dict_words(draw)
    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(possible_words)
    print("Optimal word possible: %s (value: %d)" % (max_word, max_word_score))
    print('You scored: {:.1f}'.format(word_score / max_word_score * 100))


if __name__ == "__main__":
    main()
