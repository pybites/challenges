# !python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    # pull letters from bag
    my_letters = []
    for i in range(7):
        position = random.randint(0, len(POUCH) - 1)
        # print(i, position, POUCH[position])
        my_letters.append(POUCH.pop(position))
    return my_letters


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    inp = input('Form a word with your drawn letters? ').lower()
    input_word = _validation(inp, draw)
    return input_word


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    for i in word:
        if i.isalpha() == False:
            print("Sorry you entered an unacceptable letter(s)")
            quit()
        elif i.upper() not in draw:
            print("Sorry that's not a valid word using your drawn letters...")
            quit()

    if word.lower() not in DICTIONARY:
        print("Sorry that's not a valid word in the dictionary...")
        quit()

    return word


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    words = []

    for i in range(1, 7):
        perms = []
        perms.append(_get_permutations_draw(draw, i))
        for a in perms:
            for b in a:
                # print(''.join(b))
                if ''.join(b).lower() in DICTIONARY:
                    words.append(''.join(b).lower())

    return words


def _get_permutations_draw(draw, length):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    return list(itertools.permutations(draw, length))


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
