#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    letters = [chr(random.randint(65,90)) for _ in range(NUM_LETTERS)]
    return ''.join(letters)

    pass


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""

    word = raw_input("Form a valid word")
    if (_validation(word, draw)):
        return word
    else:
        "Invalid word"
        return None
    pass



def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""

    for i in word:
        if i not in draw:
            raise ValueError('A very specific bad thing happened.')
            #return False

    f = DICTIONARY
    for line in f:
        if word  in line:
            return True
        else:
            raise ValueError('A very specific bad thing happened.')
            #return False
    pass


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    wordPerms = _get_permutations_draw(draw)
    lowerWordPerms = [x.lower() for x in wordPerms]

    f = DICTIONARY

    matches = set(lowerWordPerms).intersection(set(f))

    return matches
    pass


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    perms = []

    for i in xrange(1, len(draw) + 1):
        perms += list(itertools.permutations(draw, i))
    retPerms = [''.join(x) for x in perms]
    return retPerms

#    for n in range(1, NUM_LETTERS + 1))
#    gen_permutations_n_letters = sum(len(list(itertools.permutations(self.draw, n)))

    pass


# From challenge 01:
def max_word_value(strWord=[]):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    i = 0
    returnWord = ''
    if len(strWord) == 0:
        with open(DICTIONARY) as f:
            strWord = f.read().splitlines()

    for oneLine in strWord:
        newOneLine = ''.join(ch for ch in oneLine if ch.isalnum())
        tempValue = sum(LETTER_SCORES[c.upper()] for c in newOneLine)
        if i < tempValue:
            i = tempValue
            returnWord = oneLine
    return returnWord
    pass






def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
