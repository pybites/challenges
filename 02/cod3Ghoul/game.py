#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
from collections import Counter
from operator import contains

from data import DICTIONARY, LETTER_SCORES, POUCH


NUM_LETTERS = 7


class WordPossibilities:
    def __init__(self, players_draw):
        self.players_draw = ''.join(players_draw)
        self.valid_perms = []
        self.run = len(self.players_draw)
        self.all_perms = []

    def get_possible_dict_words(self):
        """Get all possible words from players_draw which are valid dictionary
         words. Use the _get_permutations_draw helper and DICTIONARY
         constant"""
        while 1 < self.run <= 7:
            self.all_perms = self._get_permutations_draw(self.run)
            for w in self.all_perms:
                word = ''.join(w).lower()
                if contains(DICTIONARY, word):
                    self.valid_perms.append(word)
            self.run -= 1
        return self.valid_perms

    def get_all_perms(self):
        while 1 < self.run <= 7:
            self.all_perms = self._get_permutations_draw(self.run)
            self.run -= 1
        return self.all_perms

    def _get_permutations_draw(self, cycle):
        self.possible_perms = list(itertools.permutations(
                                   self.players_draw, cycle))
        return self.possible_perms


def draw_letters():
    return random.choices(POUCH, k=NUM_LETTERS)


def input_word(players_draw):
    players_word = input('Enter a valid word from the letters you\'ve drawn: ')
    while not _validation(players_word, players_draw):
        print(f"Your word '{players_word}' is not a valid word.")
        players_word = input('Please enter a valid word from the letters'
                             'you\'ve drawn: ')
        players_word = players_word
    else:
        return players_word


def _validation(players_word, players_draw):
    """Validations: 1) only use letters of players_draw,
       2) valid dictionary word"""
    if contains(DICTIONARY, players_word.lower()):
        draw_counter = Counter(players_draw)
        word_counter = Counter(players_word.upper())
        if any(draw_counter[l] < word_counter[l] for l in word_counter):
            raise ValueError('You cannot use any letters in your draw '
                             'more than once and can only use as many of'
                             ' a letter that you have in your draw.')
        else:
            return True
    else:
        raise ValueError('Your word is not a valid word in our dictionary.')


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


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
