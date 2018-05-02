#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

"""Play a scrabble guessing game."""

from data import DICTIONARY
from data import LETTER_SCORES
from data import POUCH
import itertools
import random

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calculate word value.

    Calc a given word value based on Scrabble LETTER_SCORES mapping.
    """
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calculate the max value of a collection of words."""
    return max(words, key=calc_word_value)


def draw_letters():
    """Return list of NUM_LETTERS letters."""
    random.shuffle(POUCH)
    return POUCH[0:NUM_LETTERS]


def _get_permutations_draw(draw):
    """Return list of possible entries from draw."""
    perms = []
    for n in range(1, NUM_LETTERS+1):
        subperm = itertools.permutations(draw, n)
        perms += list(subperm)
    return perms


def get_possible_dict_words(draw):
    """Return list of possible dict words from hand."""
    poss_words = []
    permslist = _get_permutations_draw(draw)
    for perm in permslist:
        joined = ""
        for x in range(0, len(perm)):
            joined += perm[x]
        if joined.lower() in DICTIONARY and joined.lower() not in poss_words:
            poss_words.append(joined.lower())
    return poss_words


def _validation(word, draw):
    """Return error if word not valid for draw."""
    possible = get_possible_dict_words(''.join(draw))
    if word.lower() not in possible:
        raise ValueError


def main():
    """Play the game in one loop."""
    hand = draw_letters()
    possible = get_possible_dict_words(''.join(hand))
    printable_hand=', '.join(hand)
    print(f'Your hand is: {printable_hand}')
    while True:
        try:
            player_word = str(input("Form a valid word: ")).upper()
            _validation(player_word, ''.join(hand))
            break
        except ValueError:
            print("That is not a valid word for your hand. Try again...")
    print("Word chosen: {0} (value: {1})".format(
        player_word,
        calc_word_value(player_word)
        ))
    best_word = max_word_value(possible).upper()
    print("Optimal word possible: {0} (value: {1})".format(
        best_word,
        calc_word_value(best_word)
        ))
    score = 100 * (calc_word_value(player_word)/calc_word_value(best_word))
    print(f'You scored: {score:.1f}')

if __name__ == "__main__":
    main()
