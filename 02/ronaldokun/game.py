#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
"""
Author: Ronaldo S.A.Batista
Email: ronaldokun@gmail.com
Github: @ronaldokun
"""
from itertools import permutations
from random import choices

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return choices(POUCH, k=NUM_LETTERS)
# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def _validation(word: str, draw: list) -> bool:
    """Check if word can be formed from letters in draw
    :param word: word to be checked
    :param draw: set of letters to form a word
    :return: True if word can be formed from draw, False otherwise
    """
    copy = draw[:]
    for c in word:
        try:
            copy.remove(c)
        except ValueError as e:
            raise ValueError(f"The word {word} cannot be formed from the {draw}") from e
    if not in_dict(word):
        raise ValueError(f"The word {word} is not a valid one")

    return True


def in_dict(word: str) -> bool:
    """ Check if word in in DICTIONARY
    :param word: string to check
    :return: True if word is found, False otherwise
    """
    return "".join(word).lower() in DICTIONARY

def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    word = input("Insert a valid word: ").upper()
    if _validation(word, draw):
        return word

# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    return list(filter(in_dict, _get_permutations_draw(draw)))


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    return (w for k in range(1, NUM_LETTERS+1) for w in permutations(draw, k))


def main():

    draw = draw_letters()
    print(f"Letters drawn: {draw}")

    word = input_word(draw)

    word_score = calc_word_value(word)
    print(f"Word Chosen: {word} (Value: {word_score})")

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    val_max_word = calc_word_value(max_word)

    print(f"The Optimal Word for this Draw is {''.join(max_word)} (Value: {val_max_word})")
    print(f"Your Score (player_score / optimal_score) : {word_score / val_max_word * 100: .2f}")


if __name__ == "__main__":
    main()
