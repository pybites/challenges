#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

from collections import Counter

NUM_LETTERS = 7


def draw_letters():
	return random.sample(POUCH, NUM_LETTERS)


def input_word(draw):
    valid_word = False
    while valid_word == False:
        user_word = input("What word do you see in your letters? ")
        valid_word = _validation(user_word.lower(), draw)
        if valid_word != False:
            print(user_word + " is in the draw and in the dictionary.")
    return user_word


def _validation(word, draw):
    for letter in word.lower():
        if letter not in draw:
            raise ValueError("You've used a letter that's not in your draw")
            return False
    if word not in DICTIONARY:
        raise ValueError("You've use a word that's not in the dictionary")
        return False
    for key in Counter(word.upper()).keys():
        if Counter(word.upper())[key] > Counter("".join(draw))[key]:
            raise ValueError("You've used a letter that's not in your draw")
            return False
    return True


def letter_value(letter):
    return LETTER_SCORES[letter]


def calc_word_value(word):
    word_score = 0
    for character in word:
        if character.isalpha():
            word_score += letter_value(character.upper())
    return word_score


def get_possible_dict_words(draw):
    words = []
    for permutation in _get_permutations_draw(draw):
        if ''.join(permutation) in DICTIONARY:
                words.append(''.join(permutation))
    return words


def _get_permutations_draw(draw):
    permutations = []
    for count in range(1, NUM_LETTERS+1):
        for permutation in itertools.permutations(''.join(draw).lower(), count):
            permutations.append(permutation)
    return permutations


def max_word_value(words):
    max=["", 0]
    for word in words:
        score = calc_word_value(word)
        if score > max[1]:
            max = [word, score]
    return max[0]


def main():
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    
    print('Optimal word possible: {} (value: {})'.format(max_word, calc_word_value(max_word)))

    game_score = word_score / float(calc_word_value(max_word)) * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
	