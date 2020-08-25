#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
from random import sample
from itertools import permutations
from data import DICTIONARY, LETTER_SCORES, POUCH
import sys
NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters(pouch=POUCH):
    return ''.join(sample(pouch, NUM_LETTERS))


def _validation(word, draw):
    """returns True if all letters in word are in draw AND word is
       in DICTIONARY"""
    word = word.lower()
    draw = _valid_word_draw(draw)
    for c in word:
        if c in draw:
            draw.pop(draw.index(c))
        else:
            raise ValueError(f'Letter {c} not in draw')

    if word not in DICTIONARY:
        raise ValueError(f'{word} is not in DICTIONARY')


def _valid_word_draw(wd):
    if isinstance(wd, list):
        wd = list(map(str.lower, wd))
    elif isinstance(wd, str):
        wd = wd.lower()
    return wd


def _get_permutations_draw(draw):
    """returns permutations of draw in list"""
    draw = _valid_word_draw(draw)
    perm = []
    for n in range(1, NUM_LETTERS + 1):
        perm.extend([''.join(t) for t in permutations(draw, n)])
    return perm


def get_possible_dict_words(draw):
    draw = _valid_word_draw(draw)
    return list(filter(lambda p: p in DICTIONARY,
                       _get_permutations_draw(draw)))


def main():
    draw = draw_letters()
    print(f"Letters drawn: {', '.join(draw)}")
    word = input('Form a valid word: ')
    try:
        _validation(word, draw)
    except ValueError:
        print('Invalid word')
        sys.exit(0)


    value = calc_word_value(word)
    opt = max_word_value(get_possible_dict_words(draw))
    opt_value = calc_word_value(opt)
    score = value / opt_value
    print(f'Word chosen: {word} (value: {value})')
    print(f'Optimal word possible: {opt} (value: {opt_value})')
    print(f'You scored {score:.2f}')


if __name__ == "__main__":
    main()
