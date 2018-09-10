#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
import random
import itertools

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    return random.choices(POUCH, k=NUM_LETTERS)


def _validation(word, draw):
    for char in set(word):
        if draw.count(char) < word.count(char):
            raise ValueError

        if word.lower() not in DICTIONARY:
            raise ValueError


def get_possible_dict_words(draw):
    words = []
    for permutation in _get_permutations_draw(draw):
        try:
            _validation(permutation, draw)
        except ValueError:
            continue

        words.append(permutation)
    return words


def _get_permutations_draw(draw):
    permutations = (itertools.permutations(draw, n) for n in range(1, NUM_LETTERS+1))
    return map(''.join, itertools.chain.from_iterable(permutations))



# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    drawed_letters = draw_letters()
    print('Letters drawn: {}'.format(', '.join(drawed_letters)))
    while True:
        user_word = input('Form a valid word: ').upper()
        try:
            _validation(user_word, drawed_letters)
        except ValueError:
            continue
        
        optimal = max_word_value(get_possible_dict_words(drawed_letters))
        user_value, optimal_value = map(calc_word_value, (user_word, optimal))
        scored = user_value / optimal_value

        print('Word chosen: {} (value: {})'.format(user_word, user_value))
        print('Optimal word possible: {} (value: {})'.format(optimal, optimal_value))
        print('You scored: {}'.format(scored))
        break


if __name__ == "__main__":
    main()
