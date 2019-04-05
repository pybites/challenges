#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
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

def draw_letters():
    return random.sample(POUCH, 7)

def valid(word, draw):

    lst = draw.copy()
    for letter in word:
        if letter.upper() in lst:
            lst.remove(letter.upper())
        else:
            return False
    if word.lower() in DICTIONARY:
        return True
    return False

def get_possible_words(draw):

    possible = []
    for word in DICTIONARY:
        if len(word) <= 7:
            lst = draw.copy()
            for letter in word:
                if letter.upper() in lst:
                    lst.remove(letter.upper())
                else:
                    break
            else:
                possible.append(word)

    return possible

def main():
    draw = draw_letters()
    print('Letters drawn:', draw)
    word = input('Form a valid word: ')
    if valid(word, draw):
        wordval = calc_word_value(word)
        print('Word chosen: {} (value: {})'.format(word.upper(), wordval))
        wordlist = get_possible_words(draw)
        optimal = max_word_value(wordlist)
        optval = calc_word_value(optimal)
        print('Optimal word possible: {} (value: {})'.format(optimal.upper(), optval))
        print('You scored: {:.1f}'.format(wordval / optval * 100))
    else:
        print('Invalid word!')

if __name__ == "__main__":
    main()
