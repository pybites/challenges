#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES
from collections import namedtuple
from draw import (Draw, _is_valid_word)


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

    # Below 2 functions pass through the same 'draw' argument (smell?).
    # Maybe you want to abstract this into a class?
    # get_possible_dict_words and _get_permutations_draw would be instance methods.
    # 'draw' would be set in the class constructor (__init__).
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""


# re-use from challenge 01
def max_valued_word(words):
    """ from a collection of words find the word with the highest value
    and return a tuple with that word and its coresponding value """
    Valuable = namedtuple('Valuable', 'word value')
    valuable_word = sorted(words, key=calc_word_value, reverse=True)[0]
    return Valuable(valuable_word, calc_word_value(valuable_word))


def get_word(letters, dictionary=DICTIONARY):
    """ gets input from user till word is in dict and can be made
    using letters"""

    # ask for words untill word given is in lowercase dict
    valid_word = False
    while (not valid_word):
        word = input('Form a valid word: ')
        valid_word = _is_valid_word(word, letters)

    return word


def main():
    # draw letters from POUCH and print them

    draw = Draw()
    print(f'Letters drawn: {draw}')
    # get valid word from user
    word = get_word(draw)
    word_value = calc_word_value(word)
    print(f'Word chosen: {word} (value: {word_value})')
    possible_words = draw.get_possible_dict_words()
    optimal = max_valued_word(possible_words)
    print(f'Optimal word possible: {optimal.word.upper()} ({optimal.value})')
    score = (word_value / optimal.value) * 100
    print(f'You scored: {score:.1f}')


if __name__ == "__main__":
    main()
