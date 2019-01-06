#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from itertools import permutations
import random

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

# draw 7 random letters from POUCH
def draw_letters():
    draw = []
    for i in range(7):
        draw.append(random.choice(POUCH))
    return draw

# check if user word is valid
def _validation(word, draw): 
    # create local copy of draw to preserve original draw list
    local_draw = draw.copy()
    # check is word matches letters in draw
    for letter in word.upper():
        if letter not in local_draw:
            raise ValueError(f"{word} is not a valid word\n")
        else:
            # prevents duplicate letters from passing test
            local_draw.remove(letter)
        
    # check if word in dictionary
    if word.lower() in DICTIONARY:
        return True
    else:
        raise ValueError(f"{word} not in dictionary\n")

# get all possible permutations for draw
def _get_permutations_draw(draw):
    total_permutations = []
    for i in range(1, NUM_LETTERS+1):
        current_permutations = list(map("".join, permutations(draw, i)))
        total_permutations += current_permutations
    
    return total_permutations

# calculate value of max permutation in dictionary
def get_possible_dict_words(draw):  
    total_permutations = _get_permutations_draw(draw)
    return [word for word in total_permutations if word.lower() in DICTIONARY]

# main function
def main():
    
    while True:
        draw = draw_letters()

        print(f"Letters drawn: {', '.join(draw)}")
        print("(Enter \"reset\" to draw again or \"quit\" to end game)\n")
        
        valid_input = False
        while  valid_input == False:
            user_input = input("Form a valid word: ")

            if user_input.lower() == "reset":
                print("\n")
                break
            elif user_input.lower() == "quit":
                return
            else:
                print(draw)
                valid_input = _validation(user_input, draw) 

                print(f"Word chosen: {user_input} (value: {calc_word_value(user_input)})")
                print(draw)

                possible_dict_words = get_possible_dict_words(draw)
                optimal_word = max(possible_dict_words, key=calc_word_value)
                optimal_value = calc_word_value(optimal_word)

                print(f"Optimal word possible: {optimal_word} (value: {optimal_value})")

                score = calc_word_value(user_input) / optimal_value
                print(f"You scored: {round(score, 2) * 100}\n")

if __name__ == "__main__":
    main()
