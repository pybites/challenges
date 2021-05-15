#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
import itertools

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
from datetime import date
from collections import Counter

HANDS = []
NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def _get_permutations_draw(letters):
    return list(itertools.chain.from_iterable([list(itertools.permutations(letters, n)) for n in range(1, NUM_LETTERS + 1)]))

def _validation(word, letters):
    if all([True if w in letters else False for w in list(word)]):
        if word in DICTIONARY:
            return True
    raise ValueError("Word not in Letters!")

def draw_letters():
    """Takes a tile out of the pouch and puts it into the hands"""
    for n in range(NUM_LETTERS):
        HANDS.append(random.choice(POUCH))
        POUCH.remove(HANDS[-1])
    return HANDS[-7:]

def get_possible_dict_words(letters):
    word_list = []
    for word in DICTIONARY:
        if len(word) < 3:
            print(word.upper())
        if len(word) <= len(letters):
            list_word = Counter(list(word.upper()))
            list_letters = Counter(letters)
            if all([True if _ in list_letters.keys() and list_letters[_] >= list_word[_] else False for _ in list_word]):
                word_list.append(word)
    return word_list

def main():
    for n in range(NUM_LETTERS):
        draw_letters()
    pass

if __name__ == "__main__":
    random.seed(date.today())
    main()
