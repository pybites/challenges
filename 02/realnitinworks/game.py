import random
from itertools import permutations

from data import POUCH, DICTIONARY, LETTER_SCORES


NUM_LETTERS = 7


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum(
        LETTER_SCORES.get(letter, 0)
        for letter in word.upper()
    )


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = DICTIONARY

    word_values = {
        word: calc_word_value(word)
        for word in words
    }

    return max(word_values, key=word_values.get)


def draw_letters():
    """Draw NUM_LETTERS random letters from POUCH"""
    letters_drawn = [
        random.choice(POUCH)
        for _ in range(NUM_LETTERS)
    ]
    return letters_drawn


def _letters_check(word, letters_drawn):
    """Validate all letters of word are in draw"""
    return all(
        word.upper().count(letter) <= letters_drawn.count(letter)
        for letter in word.upper()
    )


def _dictionary_check(word):
    """Validate the word is in DICTIONARY"""
    return word.lower() in DICTIONARY


def _validation(word, letters_drawn):
    """Wrapper which validates the input word"""
    if not (
            _letters_check(word, letters_drawn) and
            _dictionary_check(word)
    ):
        raise ValueError("Not a valid word combination!")


def _get_permutations_draw(letters):
    """Gets all permutations of the drawn letters"""
    return [
        "".join(item)
        for n in range(1, NUM_LETTERS + 1)
        for item in permutations(letters, n)
    ]


def get_possible_dict_words(letters):
    """Filters valid dictionary words from all possible permutations"""
    return [
        word
        for word in _get_permutations_draw(letters)
        if _dictionary_check(word)
    ]


def start_game():
    """The game logic starts here"""
    letters_drawn = draw_letters()
    print(f"Letters drawn: {', '.join(letters_drawn)}")

    user_word = input("Form a valid word: ")
    _validation(user_word, letters_drawn)

    word_value = calc_word_value(user_word)
    print(f"Word chosen: {user_word} (value: {word_value})")

    optimal_word = max_word_value(
        get_possible_dict_words(letters_drawn)
    )
    optimal_word_value = calc_word_value(optimal_word)
    print(f"Optimal word possible: {optimal_word} (value: {optimal_word_value})")

    score = round(word_value/optimal_word_value*100, 1)
    print(f"You scored: {score}")


def main():
    """The main loop"""
    while True:
        command = input("\n\nScrabble Game Options: [P]lay, [Q]uit : ").upper().strip()
        if command == 'P' or command == 'PLAY':
            try:
                start_game()
            except ValueError as e:
                print(e)
        elif command == 'Q' or command == 'QUIT':
            break
        else:
            continue


if __name__ == "__main__":
    main()
