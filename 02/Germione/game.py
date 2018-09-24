#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
from itertools import permutations

from data import DICTIONARY, LETTER_SCORES, POUCH

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
    """Draw 7 letters from POUCH"""
    me_pouch = list()
    pouch_len = len(POUCH)
    for _ in range(0, 7):
        position = random.randint(0, pouch_len - 1)
        me_pouch.append(POUCH.pop(position))
        pouch_len = pouch_len - 1
    return me_pouch


def _validation(word, draw):
    """Validate if letters are in the pouch and if word is in DICTIONARY"""
    for letter in word:
        if letter.upper() not in draw:
            raise ValueError("{} is not in the draw".format(letter.upper()))

    if word not in DICTIONARY:
        raise ValueError("{} is not in the DICTIONARY")

# --------------------------------------------------------------------------- #


def all_permutations(string):

    def sub(used, left):

        combos = []

        for i in range(0, len(left)):
            ch = left.pop(i)
            used.append(ch)

            combos.append(''.join(used))

            # Append the results of the  recursive call to our combos list
            combos = combos + sub(used, left)

            # Remove ch from used
            used.pop(-1)

            # Splice ch back into left at its original index
            left[i:0] = [ch]

        return combos

    return sub([], list(string))


def all_valid_permutations(string):

    all_possible_words = all_permutations(string)
    all_valid_words = []
    for word in all_possible_words:
        if word in DICTIONARY:
            all_valid_words.append(word)

    return all_valid_words


def optimal_word(all_valid_words):

    if len(all_valid_words) == 0:
        print("No Optimal word")
        return None

    optimus_word = max_word_value(all_valid_words)
    return optimus_word


# --------------------------------------------------------------------------- #


def _get_permutations_draw(string):
    all_permutations = []
    word = "".join(string)
    for n in range(1, len(word) + 1):
        all_permutations = all_permutations + list(permutations(word, n))

    return all_permutations


def get_possible_dict_words(string):
    all_possible_words = _get_permutations_draw(string)
    all_valid_words = []
    for possible in all_possible_words:
        word = "".join(possible)
        if word.lower() in DICTIONARY:
            all_valid_words.append(word)

    return all_valid_words


def play():
    your_letters = draw_letters()
    print("Form a word with: ", your_letters)
    while True:
        try:
            word = input("Response: ")
            _validation(word, your_letters)
            break
        except ValueError:
            print("Wrong word")
            continue
    score = calc_word_value(word)
    print("Your score for {} is {}".format(word, score))


def main():
    play()


if __name__ == "__main__":
    #main()
    _get_permutations_draw("GARYTEV")

    print(list(permutations("GARYTEV", 2)))

