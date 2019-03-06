#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from random import choice
from collections import Counter
from sys import exit

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
    """
    show a 7 letter board to a user to be used for word making.
    Randomly take the letter from POUCH list
    """
    board = []
    for i in range(7):
        board.append(choice(POUCH))

    return board

def _validation(word_entered, board):
    """ 
    check all the letters in the word were given within the draw,
    check if word exists in DICTIONARY and if so, calculate word value
    """
    # if it's not a DICTIONARY word, return True
    if not word_entered in DICTIONARY:
        raise ValueError("Word not in dictonary, try again!")

    for i in word_entered:
        # if 0, the char i does not exist on board
        if board.count(i.upper()) == 0:
            raise ValueError("Input doesn't match the board, try again!")
        else:
            # remove the letter to make sure the letter is not abused
            board.remove(i.upper())

    return 


def get_possible_dict_words(board):
    """
    Check for different possible words for a given draw (board), return the most valued one.
    """
    possible_words = []
    # travel through all DICTIONARY
    for word in DICTIONARY:
        exist_flag = 1
        # we check whether word' characters are present within the board. For doing so, convert the word in a dictonary (key-character:value-occurences) to get rid of repeated values
        dicto = Counter(word)
        for i in dicto.keys():
            # check character existance:
            if i.upper() not in board:
                exist_flag = 0
            # check character occurrences
            if dicto.get(i) > board.count(i.upper()):
                exist_flag = 0

        if exist_flag == 1:
            possible_words.append(word)
    
    return possible_words


def player_score(player_score, optimal_score):
    """
    Return the player score based on the optimal word score vs the one obtained by the player.
    """
    return "{:.1f}".format(player_score * 100 / optimal_score)

# only for testing purpose, as I don't use this approach actually
def _get_permutations_draw(board):
    from itertools import permutations
    perms = []
    for i in range(len(board)):
        #perms for L=i
        i_perms = permutations(board, i+1)
        # add i_perms to perms 
        for i in list(i_perms):
            perms.append(i)

    return perms


def main():
    while True:
        board = draw_letters()
        print(f"Letters drawn: {board}")
        word_entered = input(f"Form a valid word: ").lower()
        try:
            _validation(word_entered, board)
        except ValueError as error:
            print(error)
            continue

        print(f"Word chosen: {word_entered} (value: {calc_word_value(word_entered)})")
        possible_words = get_possible_dict_words(board)
        maxword = max_word_value(possible_words)
        print(f"Optimal word possible: {maxword} (value: {calc_word_value(maxword)})")
        score = player_score(calc_word_value(word_entered),calc_word_value(maxword))
        print(f"You scored: {score}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit() 
        
