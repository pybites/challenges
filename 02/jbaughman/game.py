#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from itertools import permutations
from random import sample

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters(num_letters=NUM_LETTERS):
    """Draw a random number letters from the pouch of letters
    
    Args:
        num_letters: (int) number of letters to be drawn. Defaults to constant
        NUM_LETTERS if no value is passed.

    Returns:
    """
    return sample(POUCH, num_letters)


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum([LETTER_SCORES.get(x, 0) for x in word.upper()])


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    word_values = {calc_word_value(word): word for word in words}
    return word_values.get(max(word_values.keys()))


def get_possible_dict_words(letters):
    """
    
    Args:
        letters:

    Returns:

    """
    words = [word for word in _get_permutations_draw(letters)
             if word.lower() in DICTIONARY
             or word.title() in DICTIONARY]
    print(len(words))
    return words


def _get_permutations_draw(letters):
    perms = []
    for r in range(1, len(letters) + 1):
        for x in permutations(letters, r):
            perms.append("".join(x))
    return perms


def main():
    draw = list('garytev'.upper())
    # draw = draw_letters()
    get_possible_dict_words(draw)
    print(f"You have drawn the following letters: {', '.join(draw)}")
    word = input("Please form a word with the letters you have drawn: ")
    print(f"Your score for the word '{word}' is {calc_word_value(word)}")


if __name__ == "__main__":
    main()
