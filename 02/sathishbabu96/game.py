#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    words = []
    for _ in range(NUM_LETTERS):
        words.append(random.choice(POUCH))
    return words


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    word = input("Provide the word formed using the given letters: ")
    bonus = 0
    _validation(word, draw)
    if len(word) == 7:
        print('Wow! you have made a seven letter word. You will receive a bonus of 25 points!!.')
        bonus += 25
    return word, bonus


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    for char in word.upper():
        if char not in draw:
            raise ValueError(f"Character {char} not in {draw}")
    _dictionary = [word.upper() for word in DICTIONARY]
    if word.upper() not in _dictionary:
        raise ValueError(f"Not a valid word")


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw, r=None):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    _words = _get_permutations_draw(draw, r)
    _dictionary = [word.upper() for word in DICTIONARY]
    return set(_words).intersection(set(_dictionary))


def _get_permutations_draw(draw, r=None):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    words = []
    if not r:
        for r in range(1, NUM_LETTERS + 1):
            for word in itertools.permutations(draw, r):
                words.append("".join(word).upper())
    else:
        for word in itertools.permutations(draw, r):
            words.append("".join(word).upper())
    return words


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word, bonus = input_word(draw)
    word_score = calc_word_value(word)
    word_score += bonus
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = (word_score / max_word_score) * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
