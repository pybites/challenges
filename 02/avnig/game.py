#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from random import randint
from itertools import permutations

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return [POUCH[randint(1, len(POUCH))] for _ in range(NUM_LETTERS)]

def in_dict(word: str) -> bool:
    """ Check if word in in DICTIONARY
    :param word: string to check
    :return: True if word is found, False otherwise
    """
    return "".join(word).lower() in DICTIONARY


def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    return list(filter(in_dict, _get_permutations_draw(draw)))


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    return (w for k in range(1, NUM_LETTERS + 1) for w in permutations(draw, k))


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def input_word(draw):
    player_word = input("Make a word from the drawn letters")
    if _validation(player_word, draw):
        return player_word


def _validation(word, draw):
    for char in word:
        if char.upper() not in draw:
            return False
    if word.lower() not in DICTIONARY:
        return False
    return True


def main():
    draw = draw_letters()
    print('Letters drawn: {}'.format(','.join(draw)))

    word = input_word(draw)
    print(word)

    word_value = calc_word_value(word)
    print('The word value is {}'.format(word_value))

    possible_words = get_possible_dict_words(draw)
    print(possible_words)

    max_word = max_word_value(possible_words)
    val_max_word = calc_word_value(max_word)

    print(f"The Optimal Word for this Draw is {''.join(max_word)} (Value: {val_max_word})")
    print(f"Your Score (player_score / optimal_score) : {word_value / val_max_word * 100: .2f}")


if __name__ == "__main__":
    main()
