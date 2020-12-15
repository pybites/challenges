#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
from itertools import chain, permutations

from data import DICTIONARY, LETTER_SCORES, POUCH


NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def _permutations(iterable):
    """Returns all possible permutations of the letters in draw."""
    return chain.from_iterable(permutations(iterable, n)
                               for n in range(1, NUM_LETTERS+1))


def calc_optimal_word(draw):
    """Calculates optimal word (highest value) given the letters in draw"""
    permutations = _permutations(draw)

    valid_words = set(
        ''.join(word).lower()
        for word in permutations
        if ''.join(word).lower() in DICTIONARY
    )

    max_word = max_word_value(valid_words).upper()
    max_val = calc_word_value(max_word)
    return max_word, max_val


def draw_letters():
    """Returns 7 random letters from POUCH"""
    return [
        random.choice(POUCH)
        for _ in range(NUM_LETTERS)
    ]


def get_user_input(draw):
    """Asks the player to form a word with one or more letters from draw."""
    draw_copy = draw.copy()
    print('Letters drawn:', *draw_copy)

    while True:
        word = input('Form a valid word: ').lower()

        try:
            if word not in DICTIONARY:
                raise ValueError(f'{word} is not in the dictionary. Try again.')

            word = word.upper()
            for letter in word:
                if letter not in draw_copy:
                    raise ValueError(f'{letter} is not in draw. Try again.')
                else:
                    draw_copy.remove(letter)

            return word
        except ValueError as e:
            print(e)
            continue


def main():
    draw = draw_letters()
    word = get_user_input(draw)
    word_value = calc_word_value(word)
    print(f'Word chosen: {word} (value: {word_value})')

    optimal_word, optimal_val = calc_optimal_word(draw)
    print(f'Optimal word possible: {optimal_word} (value: {optimal_val})')

    player_score = round((word_value / optimal_val) * 100, 1)
    print(f'You scored: {player_score}')


if __name__ == "__main__":
    main()
