#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
from collections import Counter
from typing import Dict, List

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7
PERCENTAGE_MULTIPLIER = 100


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters() -> List[str]:
    return random.sample(POUCH, NUM_LETTERS)


def is_legal_word(word: str, drawn_letters_count: Dict[str, int]) -> bool:
    word_letters_count = Counter(word.upper())
    for letter, count in word_letters_count.items():
        if count > drawn_letters_count.get(letter, 0):
            return False

    return True


def get_possible_dict_words(drawn_letters: List[str]) -> List[str]:
    drawn_letters_count = Counter(drawn_letters)
    return [word for word in DICTIONARY if is_legal_word(word, drawn_letters_count)]


def main() -> None:
    drawn_letters = draw_letters()
    legal_words = get_possible_dict_words(drawn_letters)
    print(f"Letters drawn: {', '.join(drawn_letters)}")

    user_input = input("Form a valid word: ")
    while user_input not in legal_words:
        user_input = input("Nope, please try a different word: ")

    user_word = user_input.upper()
    user_score = calc_word_value(user_word)
    print(f"Word chosen: {user_word} (value: {user_score})")

    best_word = max_word_value(legal_words)
    best_score = calc_word_value(best_word)
    print(f"Optimal word possible: {best_word} (value: {best_score})")

    print(f"You scored: {PERCENTAGE_MULTIPLIER * user_score / best_score : .2f}")


if __name__ == "__main__":
    main()
