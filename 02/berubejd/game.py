#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
import sys

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters() -> list:
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.sample(POUCH, NUM_LETTERS)


def input_word(draw) -> str:
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    
    while True:
        try:
            response = input(f'Please enter a word using only the letters in your draw [ {", ".join(draw)} ]: ')
            response = response.upper()

            if _validation(response, draw):
                return response
            else:
                print(f'I\'m sorry.  That\'s not a valid combination for your letters.')

        except KeyboardInterrupt:
            sys.exit()

        except:
            pass


def _validation(word: str, draw: list) -> bool:
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""

    temp_list = draw.copy()

    if not word.lower() in DICTIONARY:
        return False

    for char in word:
        try:
            temp_list.pop(temp_list.index(char))

        except ValueError:
            return False

    return True

# From challenge 01:
def calc_word_value(word: str) -> int:
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
### From PyBites 65
def get_possible_dict_words(draw: list) -> list:
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""

    return [perm.upper() for perm in _get_permutations_draw(draw) if perm.lower() in DICTIONARY]


def _get_permutations_draw(draw: list) -> str:
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""

    for length in range(1, len(draw) + 1):
        for perm in itertools.permutations(draw, length):
            yield ''.join(perm)


# From challenge 01:
def max_word_value(words: list) -> int:
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
