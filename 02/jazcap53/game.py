#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from random import sample

from data import DICTIONARY, LETTER_SCORES, POUCH
from itertools import permutations

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES[letr.upper()] for letr in word if letr.isalpha())

def _get_valid_input(bag):
    user_word = input(f"Make an English word from the following letters: {' '.join(bag)} > ")
    print(user_word)
    while not all([c.upper() in bag for c in user_word]) or not user_word.upper() in DICTIONARY:
        if user_word.upper() in DICTIONARY:
            print(f"Oops: please choose from the following letters: {' '.join(bag)} > ")
            user_word = input()
        else:
            print(f"Oops: {user_word} is not in my dictionary. Please try again. Your letters are: {' '.join(bag)} > ") 
            user_word = input()
    return user_word

def _get_best_words(bag):
    best_score = 0
    best_words = {}
    for i in range(1, 8):
        for p in permutations(bag, i):
            if (word := ''.join(p).upper()) not in DICTIONARY:
                continue
            if (val := calc_word_value(word)) > best_score:
                best_score = val
                best_words = {word}
            elif val == best_score:
                best_words.add(word)
    return best_score, best_words

def main():
    global DICTIONARY
    DICTIONARY = {w.upper() for w in DICTIONARY if len(w) > 1 or w.upper() in 'AI'}
    bag = sample(POUCH, 7)
    user_word = _get_valid_input(bag)
    user_value = calc_word_value(user_word)
    print(f'Word chosen: {user_word.upper()}: (value: {user_value})')
    best_score, best_words = _get_best_words(bag)
    best_words_string = ', '.join(best_words)
    print(f'My best score {best_score} -- best_word(s) {best_words_string}')
    print(f'Your score: {user_value * 100 / best_score:.1f}') 


if __name__ == "__main__":
    main()
