#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUNCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=lambda w: calc_word_value(w))


def draw_letters():
    """Draw a random set of NUM_LETTERS letters. Hint: use random"""
    pass


def input_word(draw):
    """Ask user to input a word. Check vs. draw letters if user is using right letters.
    Also check if the given word is in the DICTIONARY set"""
    pass


def get_valid_dict_words(draw):
    """Take the draw letters, calculate all possible words, then cross-check with DICTIONARY (= set).
    Return the result. Hint: use itertools.permutations and set operations."""
    pass


def main():
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} with value: {}'.format(word, word_score))

    possible_words = get_valid_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Max word: {} with value: {}'.format(max_word, max_word_score))

    game_score = float(word_score) / max_word_score * 100
    print('You scored: {}'.format(game_score))
    
    # bonus: make scores persistent and delight user when he/she breaks a new record

if __name__ == "__main__":
    main()
