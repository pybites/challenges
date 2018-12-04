#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from random import sample
from itertools import permutations

NUM_LETTERS = 7

def draw_letters():
    return sample(POUCH,NUM_LETTERS)

def get_possible_dict_words(letters):
    return _get_permutations_draw(letters) & DICTIONARY

def _get_permutations_draw(letters):
    return {''.join(word).lower() for i in range (1,8) for word in permutations(letters, i)}

def _validation(word, letters, possible = None):
    if possible == None:
        possible = get_possible_dict_words(letters)
    if word not in possible:
        raise ValueError('Create a valid word using the drawn letters')

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    letters = draw_letters()
    possibles = get_possible_dict_words(letters)
    
    print('Letters drawn: ' + ', '.join(letters))
    while True:
        try:
            word = input('Form a valid word: ')
            _validation(word.lower(), letters, possibles)
            break
        except ValueError:
            print('Please create a valid word using the drawn letters')

    score = calc_word_value(word)
    best_word = max_word_value(possibles)
    best_score = calc_word_value(best_word)
    
    print('Word chosen: {} (value: {})'.format(word.upper(), score))
    print('Optimal word possible: {} (value: {})'.format(best_word.upper(), best_score))
    print('You scored: {:.1f}'.format(score * 100 / best_score))
    

          
if __name__ == "__main__":
    main()
