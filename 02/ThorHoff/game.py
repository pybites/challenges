#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
import itertools
from copy import deepcopy

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def _get_permutations_draw(letters: list) -> list:
    permutations = []
    for i in range(1, len(letters) + 1):
        permutations += ["".join(permutation) for permutation in itertools.permutations(letters, i)]
    return permutations


def _validation(word: str, letters: list):
    if word.lower() not in DICTIONARY:
        raise ValueError("Word not in Dictionary!")
    for char in word:
        letters.remove(char.upper())


def get_possible_dict_words(letters: list) -> list:
    permutations = _get_permutations_draw(letters)
    words = [word for word in permutations if word.lower() in DICTIONARY]
    return words


def draw_letters():
    return random.choices(POUCH, k=7)


def game_result(letters: list, word=None):
    poss_words = get_possible_dict_words(letters)
    best_choice = max_word_value(poss_words)
    best_choice_value = calc_word_value(best_choice)
    if word:
        word_value = calc_word_value(word)
        print(f"Word chosen: {word} (value: {word_value})")
    print(f"Optimal word possible: {best_choice} (value: {best_choice_value})")
    if word:
        print(f"You scored: {100 * word_value / best_choice_value}")


def main():
    letters = draw_letters()
    while True:
        print(f"Letters drawn: {letters}")
        word = input("Form a valid word: ")
        try:
            _validation(word, deepcopy(letters))
            game_result(letters, word)
            new_game = input("To quit the game press q and to play a new round "
                             "press any key: ")
            if new_game.lower() == "q":
                break
            else:
                letters = draw_letters()
        except ValueError:
            game = input("Invalid word! To try a new word press any key, to "
                         "quit press q and to get a new set of words press n: ")
            if game.lower() == "q":
                game_result(letters)
                break
            elif game.lower() == "n":
                game_result(letters)
                letters = draw_letters()


if __name__ == "__main__":
    main()
