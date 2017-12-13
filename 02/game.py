#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
import itertools

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.sample(POUCH, NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    print("Letters drawn: {}".format(draw))

    while True:
        word = input("Form a valid word: ")
        try:
            return _validation(word, draw)
        except ValueError as e:
            print(e)
            continue


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""

    for letter in word.upper():
        if letter in draw:
            draw.remove(letter)
        else:
            raise ValueError("Letter '{}' is not in a draw !!".format(letter))

    if not word.lower() in DICTIONARY:
        raise ValueError('Not a valid dictionary word !!  Try again.')

    return word


def _get_permutations_draw(draw):
    return [''.join(word).lower() for i in range(1, NUM_LETTERS + 1) for word in itertools.permutations(draw, i)]


def get_possible_dict_words(draw):
    return set(_get_permutations_draw(draw)) & set(DICTIONARY)


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    draw = draw_letters()
    word = input_word(draw)
    print("Word chosen: {} (value: {})".format(word, calc_word_value(word)))

    optimal_word = max_word_value(get_possible_dict_words(draw))
    print("Optimal word possible: {} (value: {})".format(optimal_word, calc_word_value(optimal_word)))


if __name__ == "__main__":
    main()
