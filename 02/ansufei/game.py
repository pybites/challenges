#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
from itertools import combinations,permutations
import re

NUM_LETTERS = 7

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.sample(POUCH, NUM_LETTERS)

def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    #Check that input letters are in the draw
    it=iter(sorted(draw))
    word_in_list=all(c in it for c in sorted(word))
    if word_in_list==False:
        print('Please only use letters from the list. Each letter drawn can only be used once.')
        raise ValueError
    #Find if the user input is a word
    with open('dictionary.txt') as f:
        dic=f.readlines()
    dic=[x.replace('\n','').upper() for x in dic]
    in_dic=''.join(word) in dic
    if in_dic==False:
        print('Your word is not in the dictionary')
        raise ValueError
    else:
        print('Word chosen: {} (value:{})'.format(word,calc_word_value(word)))
        
def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    print('Letters drawn:',draw)
    user_input = input("Form a valid word: ").upper()
    #Check that it is formed with only letters
    bCmdValid = re.match(r'^([A-Za-z]*)$', user_input, flags=re.I) is not None
    if bCmdValid == False:
        raise IndexError 
    _validation(user_input,draw)
    return user_input

def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    #Find which of these combinations are words
    with open('dictionary.txt') as f:
        dic=f.readlines()
    dic=[x.replace('\n','').upper() for x in dic]
    list_words=list(set(dic).intersection(_get_permutations_draw(draw)))
    return list_words

def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    #Make all possible combinations of the picked letters
    list_combinations=[]
    for s in range(1,NUM_LETTERS+1):
        for comb in combinations(draw, s):
            perms = [''.join(p) for p in permutations(comb)]
            list_combinations.append(perms)
    list_combinations=[item for sublist in list_combinations for item in sublist]
    return list_combinations

def main():
    pick=draw_letters()
    word_user=input_word(pick)
    list_words=get_possible_dict_words(pick)
    #Pick the word with the highest score
    optimal_word=max_word_value(list_words)
    optimal_score=calc_word_value(optimal_word)
    print('Optimal word possible: {} (value: {})'.format(optimal_word,optimal_score))
    pass

if __name__ == "__main__":
    main()
