#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
import copy
import random
from collections import Counter
from pprint import pprint

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

dictionary = dict()


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def pick_letters(cnt: int = NUM_LETTERS, pouch: list = None) -> list:
    pick = []
    for i in range(cnt):
        r = random.randint(1, len(pouch))
        pick.append(pouch.pop(r - 1))
    return pick


def validate_word_in_letters(letters, guess):
    lcount = Counter(letters)
    gcount = Counter(guess.upper())
    return len(gcount - lcount) == 0


def validate_word_in_dictionary(guess):
    return guess.upper() in dictionary


def present_to_user(letters):
    word_value = 0
    guess = input(f'Enter a word using the letters {letters} alone: ')
    if validate_word_in_letters(letters, guess) and validate_word_in_dictionary(guess):
        word_value = calc_word_value(guess)
        print(f'That is a correct word worth {word_value} points')
    else:
        print('Sorry, invalid word')
    pouch_count = Counter(letters)
    acceptable_words = {k: calc_word_value(k) for (k, v) in dictionary.items() if len(v - pouch_count) == 0}
    if len(acceptable_words.items()) > 0:
        best_word = max(acceptable_words.items(), key=lambda k: k[1])
        print(f'the best word I found is {best_word[0]} worth {best_word[1]} points')
        player_score = float(word_value) / float(best_word[1])
        print(f'Your score is {player_score :.2f}{", you matched me!" if player_score == 1.0 else ""}')
    else:
        print('I found no possible words')


def main():
    # refine the dictionary for processing
    global dictionary
    dictionary = {x.upper(): Counter(x.upper()) for x in DICTIONARY}
    # copy the pouch so that tiles can be removed from it
    pouch = copy.deepcopy(POUCH)
    # print(f'size of pouch, before: {len(pouch)}')
    letters = pick_letters(NUM_LETTERS, pouch)
    # print(f'size of pouch, after: {len(pouch)}')
    present_to_user(letters)


if __name__ == "__main__":
    main()
