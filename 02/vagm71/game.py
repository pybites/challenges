#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from random import sample
from itertools import permutations

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    maxValue = 0
    maxWord = ''

    for word in words:
        score = calc_word_value(word)
        if score > maxValue:
            maxValue = score
            maxWord = word
        elif score == maxValue:
            maxWord += f' {word}'
        else:
            continue

    return maxWord


def draw_letters():
    return sample(POUCH, NUM_LETTERS)


def _validation(word, rack):
    if word.upper() not in get_possible_dict_words(rack):
        raise ValueError(f'{word.upper()} not in Dictionary or letters used not from rack')            
    else:
        return

def _get_permutations_draw(rack):
    """Helper function to find all possible permutations of the rack"""
    n = 8
    string = ''

    while n != 1:
        n = n - 1

        for perm in permutations(rack, n):
            variant = ''
            for char in perm:
                variant += char
            string += f'{variant} '

    return string.strip().split()


def get_possible_dict_words(rack):
    possWords = _get_permutations_draw(rack)
    wordList = []

    for i in possWords:
        if i.lower() in DICTIONARY:
            wordList.append(i)
        else:
            continue

    return list(set(wordList))

            
def main():
    # get 7 letters from the POUCH
    rack = draw_letters()
    print(f'Letter rack: {rack}')

    # get word from player and
    # validate if word is in the DICTIONARY
    # and if word is made from letters from the rack
    while True:
        word = input('Form a valid word using letters from the rack: ')
        try:
            _validation(word, rack)
            break
        except ValueError as error:
            print(error)
            continue

    # generate results
    wordVal = calc_word_value(word)
    maxWord = max_word_value(get_possible_dict_words(rack))
    score = round(wordVal/calc_word_value(maxWord.split()[0]), 2)

    # show results to player
    print(f'Player {word.upper()} value: {wordVal}')
    print(f'Word(s) with highest value: {maxWord}: {calc_word_value(maxWord.split()[0])}')
    print(f'Player score: {score}')

    
if __name__ == "__main__":
    main()
