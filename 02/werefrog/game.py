#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random

from collections import Counter
from itertools import permutations

from data import DICTIONARY, LETTER_SCORES, POUCH


NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters(num_letters=NUM_LETTERS, pouch=POUCH):
    """Generate a list of letters from pouch. The length is num_letters."""
    return random.sample(pouch, num_letters)


def _validation(word, draw, dictionary=DICTIONARY):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    word = word.upper()
    if not _validation_against_draw(word, draw):
        raise ValueError(f"Word not valid: {word} cannot be made from {''.join(draw)}")
    if word.lower() not in dictionary:
        raise ValueError(f"Word not valid: {word} not in dictionary")
    return word.upper()


def input_word(draw):
    """Get user's word. If word does not validate, return a dummy string."""
    word = input("Form a valid word: ")
    try:
        word = _validation(word, draw)
    except ValueError as e:
        print(e)
        word = ""
    return word


def _validation_against_draw(word, draw):
    """Check that all letters for writing word are available in draw."""
    word = word.upper()
    word_counter, draw_counter = Counter(word), Counter(draw)
    for letter in word_counter:
        in_word, in_draw = word_counter.get(letter, 0), draw_counter.get(letter, 0)
        if in_word > in_draw:
            return False
    return True


def _get_permutations_draw(draw):
    """Get all permutations of draw letters. Helper function."""
    words = []
    for r in range(1, NUM_LETTERS + 1):
        words += ["".join(letters) for letters in permutations(draw, r)]
    return words


def get_possible_dict_words(draw, dictionary=DICTIONARY):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    return [word for word in _get_permutations_draw(draw) if word.lower() in dictionary]


def main():
    draw = draw_letters()
    print("Letters drawn: ", ", ".join(draw))

    word = input_word(draw)
    score = calc_word_value(word)
    print(f"Word chosen: {word} (value: {score})")

    possible_words = get_possible_dict_words(draw)
    best_word = max_word_value(possible_words)
    best_score = calc_word_value(best_word)
    print(f"Optimal word possible: {best_word} (value: {best_score})")

    game_score = score / best_score * 100
    print(f"You scored: {game_score:.1f}")


if __name__ == "__main__":
    main()
