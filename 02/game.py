#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH
from data import _load_words
NUM_LETTERS = 7


class Game:

    def __init__(self):
        count = 0
        draw = list()
        while count != NUM_LETTERS:
            draw.append(random.choice(POUCH))
            count += 1
        self.draw = draw

    def get_possible_dict_words(self):
        all_possible = self._get_permutations_draw()
        joined_words = list()
        dict_words = list()
        for word_list in all_possible:
            joined_words.append("".join(word_list))
        for word in joined_words:
            if word.lower() in DICTIONARY:
                dict_words.append(word)
        if not dict_words:
            assert "Could not find any dictonary words with draw: {}".format(self.draw)
        return dict_words

    def _get_permutations_draw(self):
        """Helper for get_possible_dict_words to get all permutations of draw letters.
        Hint: use itertools.permutations"""
        all_perms = list()
        flat_list = list()
        for n in range(1, len(self.draw) + 1):
            all_perms.append(list(itertools.permutations(self.draw, n)))
        for sublist in all_perms:
            for item in sublist:
                flat_list.append(item)
        return flat_list


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    user_input = raw_input("Form a valid word:")
    _validation(user_input, draw)
    return user_input


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    if len(word) > len(draw):
        raise ValueError("User has chosen a word which is longer than allowed")
    dictionary_words = _load_words()
    for letter in word:
        if letter.upper() not in draw:
            raise ValueError("Letter {} not in the drawn list of letters {}".format(letter.upper(), draw))
        draw.remove(letter.upper())
    if word.lower() not in dictionary_words:
        raise ValueError('The word :{} is not in dictionary'.format(word))


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    letters = LETTER_SCORES.keys()
    word_score = 0
    for x in range(len(word)):
        letter = word[x].upper()
        if letter in letters:
            letter_score = LETTER_SCORES[letter]
            word_score += letter_score
    return word_score


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    game = Game()
    print('Letters drawn: {}'.format(', '.join(game.draw)))

    word = input_word(game.draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = game.get_possible_dict_words()

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
