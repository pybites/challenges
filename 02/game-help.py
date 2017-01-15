#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def calc_word_value(word):
    """From challenge 01:
    Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """From challenge 01:
    Calc the max value of a collection of words"""
    return max(words, key=lambda w: calc_word_value(w))


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    pass


def input_word(draw):
    """Ask player for a word. Validations: 1) only use letters of draw, 2) valid dictionary word"""
    pass


def get_possible_dict_words(draw):
    """Generate a collection of all possible words in DICTIONARY (set) from draw of NUM_LETTERS
    Hint: use itertools.permutations"""
    pass


def main():
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
