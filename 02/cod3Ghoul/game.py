#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
from collections import Counter
from operator import contains

from data import DICTIONARY, LETTER_SCORES, POUCH


NUM_LETTERS = 7
valid_perms = []
possible_perms = []


class WordPossibilities:
    def __init__(self, players_draw):
        self.players_draw = ''.join(players_draw)

    def get_possible_dict_words(self):
        """Get all possible words from players_draw which are valid dictionary words.
        Use the _get_permutations_draw helper and DICTIONARY constant"""
        run = len(self.players_draw)
        for c in range(run):
            all_perms = self._get_permutations_draw(run)
            for w in all_perms:
                word = ''.join(w).lower()
                if contains(DICTIONARY, word):
                    valid_perms.append(word)
            run -= 1
        return valid_perms

    def _get_permutations_draw(self, cycle):
        possible_perms = itertools.permutations(self.players_draw, cycle)
        return list(possible_perms)


def draw_letters():
    return random.choices(POUCH, k=NUM_LETTERS)


def input_word(players_draw):
    players_word = input('Enter a valid word from the letters you\'ve drawn: ')
    while not _validation(players_word, players_draw):
        print(f"Your word '{players_word}' is not a valid word.")
        players_word = input('Please enter a valid word from the letters you\'ve drawn: ')
        players_word = players_word
    else:
        return players_word


def _validation(players_word, players_draw):
    """Validations: 1) only use letters of players_draw, 2) valid dictionary word"""
    counter_draw = Counter(players_draw)
    if contains(DICTIONARY, players_word.lower()):
        for letter in players_word.upper():
            if contains(counter_draw, letter):
                is_valid = True
                counter_draw[letter] -= 1
                if counter_draw[letter] == 0:
                    del counter_draw[letter]
            else:
                return False
    return True


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
    max_word = max_word_value(possible_words.get_possible_dict_words())
    max_word_score = calc_word_value(max_word)
    print(f"Optimal word possible: {max_word} (value: {max_word_score})")

    game_score = round(word_score / max_word_score * 100, 1)
    print(f'You scored: {game_score}.')


if __name__ == "__main__":
    main()
