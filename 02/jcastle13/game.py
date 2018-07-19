#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    print("draw_letters method here")
    #print(random.randrange(NUM_LETTERS))
    temp_str = []
    for i in range(0,NUM_LETTERS):
        #print(POUCH[random.randrange(27)])
        temp_str.append(POUCH[random.randrange(27)])

    #print("random string:", temp_str)
    return(temp_str)

    pass


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    pass 



def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    print("validation method here")
    print("word:", word)
    print("draw:", draw)

    temp_list = list(draw)
    for i in word.upper():
        if i in temp_list:
            print("foo")
            temp_list.remove(i)
        else:
            raise ValueError("Not a valid word")

    if not word.lower() in DICTIONARY:
        raise ValueError("Not valid in dictionary")

    return (word)
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
    print("draw:", draw)

    perm = len(_get_permutations_draw(draw))
    temp_word = ""

    possible_comb = []
    print("permutation possibilities:", perm)
    for i in _get_permutations_draw(draw):
        #print("i:", i)

        temp_word = "".join(i).lower()
        #print("i_str:", temp_word)
        if temp_word in DICTIONARY:
            #print("Found a match:", temp_word)
            possible_comb.append(temp_word)

    return(possible_comb)
    pass


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    #print("draw:", draw)

    value = 0
    return_list = []
    #print("length of draw:", len(draw))
    for i in range(1,len(draw)+1):
        value = value + len(list(itertools.permutations(draw,i)))
        #return_list.append(list(itertools.permutations(draw,i)))
        #print("DEBUG:", return_list)
        for x in list(itertools.permutations(draw,i)):
            #print("x:",x)
            return_list.append(x)
            #print("LENGTH:", len(return_list))
        #print("value:", value)

    #print("length:", len(return_list))
    #print("RET:", return_list)
    return(return_list)

    pass


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


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
