#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words=None):
    """Calc the max value of a collection of words"""
    words = DICTIONARY if not words else words
    return max(words, key=calc_word_value)


def gen_draw(n=NUM_LETTERS):
    """Generate a draw of N letters from POUCH"""
    return random.sample(POUCH, n)


def is_letters_in_draw(word, draw):
    """Validate letters in word are in draw"""
    # All letters in draw must be uppercase
    valid = True
    draw = draw[:]
    for letter in word.upper():
        if letter not in draw:
            valid = False
            break
        draw.remove(letter)
    return valid


def is_word_in_dict(word):
    """Validate word exist in provided dictionary"""
    # All words in dict must be lowercase
    return word.lower() in DICTIONARY


def calc_optimal_word(draw):
    """Return a tuple with the optimal word in dictionary and its value for given draw"""
    words_n_length = {
        word
        for word in DICTIONARY
        if len(word) <= NUM_LETTERS and is_letters_in_draw(word, draw)
    }
    optimal_word = max_word_value(words_n_length)
    optimal_value = calc_word_value(optimal_word)
    return (optimal_word, optimal_value)


def calc_user_score(player_value, optimal_value):
    """Give the player a score based on player_score / optimal_score"""
    return player_value / optimal_value


def main():
    """Play a round of scrabble game with a random draw and get a score"""
    my_draw = gen_draw()
    print(f"My draw: {my_draw}")
    valid_word = False
    while not valid_word:
        my_word = input("Provide word from draw: ")
        if not is_letters_in_draw(my_word, my_draw):
            print(f"Provided word ({my_word}) not valid with given draw.")
            continue
        if not is_word_in_dict(my_word):
            print(f"Provided word ({my_word}) does not exist in defined dictionary.")
            continue
        valid_word = True
    word_value = calc_word_value(my_word)
    print(f"Word value ({my_word}): {word_value}")
    optimal_word, optimal_value = calc_optimal_word(my_draw)
    user_score = calc_user_score(word_value, optimal_value)
    print(f"Optimal Solution: ")
    print(f"Word: {optimal_word} Value: {optimal_value}")
    print(f"Your Score: {user_score:>2f}")


if __name__ == "__main__":
    main()
