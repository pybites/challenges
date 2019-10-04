#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Get random letters from the pot"""
    return random.sample(POUCH, NUM_LETTERS)

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def process_word(letters):
    while True:
        word = input("Enter your word\n").upper()
        print(f'your word is {word}\n')
        print(set(letters))
        print(set(word))
        print(len(letters)-len(word))
        print((len(letters)-len(word))+len(word))
        if len(word) == 0:
            print("Couldn't get a word? Want to quit? If you do press y")
            quit = input("y or n")
            if quit == "y":
                exit()
        elif len(word) > 7:
            print("You need to use the letters shown")
            print(*letters)
        elif set(letters).issuperset(set(word)) and (len(letters)-len(word))+len(word) == 7:
            print('Good word')
            break
        else:
            print("its broken You need to use the letters shown")
            print(*letters)

    return(word)


def main():
    letters = draw_letters()
    print(*letters)
    get_word = process_word(letters)
    if get_word in DICTIONARY:
        print("congratulations you have chosen a correct word")
        score = calc_word_value(get_word)
    else:
        print("Word not in the dictionary.")
    



if __name__ == "__main__":
    main()
