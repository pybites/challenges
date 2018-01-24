#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
from operator import contains

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7
players_draw = []
players_word = ''


class WordPossibilities(itertools.permutations):
	
	def __init__(self, players_draw):
	    self.players_draw = players_draw
	    self.perms = list(permutations(self.players_draw.sort()))
	
	
	def get_possible_dict_words(self):
	    """Get all possible words from players_draw which are valid dictionary words.
	    Use the _get_permutations_draw helper and DICTIONARY constant"""
	    return list(filter(lambda word: word in DICTIONARY, self.perms))


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.choices(POUCH, k=NUM_LETTERS)


def input_word(players_draw):
    """Ask player for a word and validate against players_draw.
    Use _validation(players_word, players_draw) helper."""
    players_word = input('Enter a valid word from the letters you\'ve drawn: ')
    while not _validation(players_word, players_draw):
        print(f"Your word '{players_word}' is not a valid word.")
        players_word = input('Please enter a valid word from the letters you\'ve drawn: ')
    else:
        return players_word


def _validation(players_word, players_draw):
    """Validations: 1) only use letters of players_draw, 2) valid dictionary word"""
    if contains(DICTIONARY, players_word):
        for letter in list(players_word.upper()):
            if contains(players_draw, letter):
                return True
            else:
                return False


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    players_draw = draw_letters()
    print(f"Letters drawn: {', '.join(players_draw)}")
    players_word = input_word(players_draw)
    word_score = calc_word_value(players_word)
    print(f"Your word '{players_word}' scores you {word_score} points.")

    possible_words = WordPossibilities(players_draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print(f"Optimal word possible: {max_word} (value: {max_word_score})")

    game_score = round(word_score / max_word_score * 100, 1)
    print(f'You scored: {game_score}.')


if __name__ == "__main__":
    main()
