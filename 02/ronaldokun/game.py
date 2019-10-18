#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from itertools import permutations
from random import choices

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


def validate(word: str, draw: list) -> bool:
    for c in word:
        try:
            draw.remove(c)
        except ValueError:
            return False
    else:
        return True


def in_dict(word: str) -> bool:
    return "".join(word).lower() in DICTIONARY


def main():
    draw = choices(POUCH, k=NUM_LETTERS)
    print(f"Letters drawn: {draw}")
    word = input("Insert a valid word: ").upper()
    if not validate(word, draw):
        print(f"The word {word} cannot be formed from the {draw}")
        return
    if not in_dict(word):
        print(f"The word {word} is not a valid one")
        return

    print(f"Word Chosen: {word} (value: {calc_word_value(word)})")

    print(list((filter(in_dict, permutations("".join(draw))))))

    # print(f"The Optimal Word for this Draw is {''.join(max_word)}")
    # print(f"Value: {calc_word_value(max_word)}")


if __name__ == "__main__":
    main()
