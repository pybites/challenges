#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
import itertools

NUM_LETTERS = 7

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word.upper():
        if letter in LETTER_SCORES.keys():
            score += LETTER_SCORES[letter]
    return score

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words==None:
        words = parse_dictionary()
    
    maximum = ("None", 0)

    for word in words:
        score = calc_word_value(word)
        if score > maximum[1]:
            maximum = (word,score)
    return maximum[0]

def draw():
    return [random.choice(POUCH) for i in range(NUM_LETTERS)]

def create_words(hand):
    tup_list = []

    for i in range(7):
        tup_list.extend(list(itertools.permutations(hand,i)))

    possible = list("".join(tuple_word).lower() for tuple_word in tup_list)

    return set(possible) & DICTIONARY

def parse_dictionary():
    return [word for word in DICTIONARY]

def check_words(hand):
    return set(hand) & set(DICTIONARY) 

def main():
    user_hand = draw()
    possible_words = create_words(user_hand)

    if possible_words:
        return max_word_value(possible_words)
    else:
        print("No possible words for this draw")

#if __name__ == "__main__":
#    main()

print(main())