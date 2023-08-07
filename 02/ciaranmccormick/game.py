#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
from collections import Counter
from itertools import permutations
from typing import List

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word: str) -> int:
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words: List[str]) -> str:
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters() -> List[str]:
    return random.choices(POUCH, k=7)


def get_possible_dict_words(draw: List[str]) -> List[str]:
    valid_permuations = [
        per for per in _get_permutations_draw(draw) if per.lower() in DICTIONARY
    ]
    return valid_permuations


def _get_permutations_draw(draw: List[str]):
    perms = list()
    for i in range(1, len(draw) + 1):
        p = ["".join(per) for per in permutations(draw, i)]
        perms += p

    return perms


def _validation(word: str, draw: List[str]) -> None:
    draw = [l.lower() for l in draw]
    draw_counter = Counter(draw)
    word_counter = Counter(word.lower())

    if not word.lower() in DICTIONARY:
        raise ValueError

    for letter, count in word_counter.items():
        if word_counter[letter] > draw_counter.get(letter, 0):
            raise ValueError


def main():
    draw = draw_letters()
    inp = input(f"Create a word from {', '.join(draw)}: ")

    try:
        _validation(inp, draw)
    except ValueError:
        print(f"'{inp}' is not a valid word.")
    else:
        score = calc_word_value(inp)
        print(f"You scored {score} for {inp.upper()}")
        all_valid = get_possible_dict_words(draw)
        top_word = max_word_value(all_valid)
        top_score = calc_word_value(top_word)
        print(f"The top word was {top_word} with {top_score}.")
        print(f"Your adjusted score is {score / top_score}")


if __name__ == "__main__":
    main()
