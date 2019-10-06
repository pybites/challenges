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


def ask_for_word(draw):
    """Get user's word. If word does not validate, return a dummy string."""
    print("Your Draw: ".ljust(12), "".join(draw))
    word = input("Your play: ".ljust(13))
    return word if validate_word(word, draw) else "-" * NUM_LETTERS


def validate_word_against_draw(word, draw):
    """Check that all letters for writing word are available in draw."""
    word = word.upper()
    word_counter, draw_counter = Counter(word), Counter(draw)
    for letter in word_counter:
        in_word, in_draw = word_counter.get(letter, 0), draw_counter.get(letter, 0)
        if in_word > in_draw:
            return False
    return True


def validate_word(word, draw, dictionary=DICTIONARY):
    """Check if the word is valid against the draw and the dictionary."""
    if not validate_word_against_draw(word, draw):
        print("Invalid: ".ljust(12), f"Cannot form {word.upper()} with {''.join(draw)}")
        return False
    if word.lower() not in dictionary:
        print("Invalid: ".ljust(12), "Not in the dictionary")
        return False
    return True


def search_best_word(draw, r=None, dictionary=DICTIONARY):
    """Given a draw, search for the best score word within dictionary."""
    best_word = ""
    for r in range(1, NUM_LETTERS + 1):
        words = ["".join(word).lower() for word in permutations(draw, r) if "".join(word).lower() in dictionary]
        if words:
            word = max(words, key=calc_word_value)
            best_word = max((best_word, word), key=calc_word_value)
    return best_word


def main():
    draw = draw_letters()
    word = ask_for_word(draw)
    score = calc_word_value(word)
    best_word = search_best_word(draw)
    best_score = calc_word_value(best_word)

    print("Your score: ".ljust(12), f"{score}/{best_score} pts [{best_word}]")


if __name__ == "__main__":
    main()
