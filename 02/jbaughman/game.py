#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from itertools import permutations
from random import sample

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters(num_letters=NUM_LETTERS):
    """Draw a random number letters from the pouch of letters
    
    Args:
        num_letters: (int) number of letters to be drawn. Defaults to constant
        NUM_LETTERS if no value is passed.

    Returns:
    """
    return sample(POUCH, num_letters)


def _validation(word, draw):
    """Helper function for validation of word input
    
    Args:
        word: (str) word submitted by player
        draw: (list) list of drawn letters

    Returns: None.
    
    Raises: ValueError on failed validation.

    """
    validate = True
    word = word.upper()
    for l in word:
        if l not in draw or draw.count(l) < word.count(l):
            validate = False
    if word.title() not in DICTIONARY and word.lower() not in DICTIONARY:
        validate = False
    if not validate:
        raise ValueError
    return None


def input_word(draw):
    """Gets word from user and validates the word against the dictionary and
    the drawn letters
    
    Args:
        draw: (list) Letters drawn

    Returns: (str) validated word

    """
    word = input("Please form a word with the letters you have drawn: ")
    try:
        _validation(word, draw)
        return word
    except ValueError:
        print("That is not a valid word. Please try again.")
        return None


# re-use from challenge 01
def calc_word_value(word=None):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping
    
    Args:
        word: (str) Word provided by user
    """
    return sum([LETTER_SCORES.get(x, 0) for x in word.upper()])


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words
    
    Args:
        words: (list) list of words to compare values
        
    Returns:
        (int) The maximum value of the list of words' values
    """
    word_values = {calc_word_value(word): word for word in words}
    return word_values.get(max(word_values.keys()))


def get_possible_dict_words(letters):
    """Returns valid words from all permutations of given letters
    
    Args:
        letters: list[str] the letters used to form the words

    Returns: list of possible dict words

    """
    words = [word for word in _get_permutations_draw(letters)
             if word.title() in DICTIONARY
             or word.lower() in DICTIONARY]
    return words


def _get_permutations_draw(letters):
    perms = []
    for r in range(1, len(letters) + 1):
        for x in permutations(letters, r):
            perms.append("".join(x))
    return perms


def play_game():
    draw = draw_letters()
    print(f"You have drawn the following letters: {', '.join(draw)}")
    word = None
    while not word:
        word = input_word(draw)
    player_score = calc_word_value(word)
    print(f"The word '{word}' has a score of {player_score}.")
    best_word = max_word_value(get_possible_dict_words(draw))
    best_word_score = calc_word_value(best_word)
    print(
            f"The best word from these letters is "
            f"{best_word}, with a score of {best_word_score}.")
    print(f"Your score is {player_score / best_word_score:.1f}.")


def main():
    play_game()


if __name__ == "__main__":
    main()
