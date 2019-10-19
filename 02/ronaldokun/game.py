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

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def validate(word: str, draw: list) -> bool:
    """Check if word can be formed from letters in draw
    :param word: word to be checked
    :param draw: set of letters to form a word
    :return: True if word can be formed from draw, False otherwise
    """
    copy = draw[:]
    for c in word:
        try:
            copy.remove(c)
        except ValueError:
            return False
    else:
        return True


def in_dict(word: str) -> bool:
    """ Check if word in in DICTIONARY
    :param word: string to check
    :return: True if word is found, False otherwise
    """
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

    val_word = calc_word_value(word)
    print(f"Word Chosen: {word} (Value: {val_word})")

    k = NUM_LETTERS

    while k >= 0:
        max_word = sorted(filter(in_dict, permutations("".join(draw), k)), key=calc_word_value, reverse=True)
        if max_word:
            break
        else:  # there is not a word from this draw and NUM_LETTERS
            k -= 1

    max_word = "".join(max_word[0])
    val_max_word = calc_word_value(max_word)

    print(f"The Optimal Word for this Draw is {''.join(max_word)} (Value: {val_max_word})")
    print(f"Your Score (player_score / optimal_score) : {val_word / val_max_word: .2f}")


if __name__ == "__main__":
    main()
