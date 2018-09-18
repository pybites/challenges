"""Play Hangman with movie titles."""

from graphics import hang_graphics
from movies import get_movie as get_word  # keep interface generic
from string import ascii_uppercase
from string import digits
import sys

ASCII = list(ascii_uppercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    """Define the game."""

    def __init__(self, word='password', guess=0, win=False):
        """Set up the game."""
        self.word = word.upper()
        self.guess = guess
        self.masked = Hangman.mask_word(self.word)
        self.chosen = []
        self.win = win

    def mask_word(word):
        """Create masked word string."""
        word_list = word.split()
        for word, value in enumerate(word_list):
            mask_word = ""
            for char in value:
                if char in ascii_uppercase:
                    mask_word += PLACEHOLDER
                else:
                    mask_word += char
            word_list[word] = mask_word
        masked = ' '.join(word_list)
        return masked

    def __str__(self):
        """Define the printer friendly game state."""
        if self.guess == 0:
            return f'Here is your word/phrase:\n{self.masked}'
        else:
            fmt = "{0:<}\n\n{1:<}\n{2:<}"
            return fmt.format(HANG_GRAPHICS[self.guess-1],
                              "Here is your word/phrase: ",
                              self.masked)


def validate_word(word):
    """Make sure the word / phrase doesn't have numbers."""
    for char in word:
        if char in digits:
            return True
    return False


def get_user_guess():
    """Get user input."""
    choice = 0
    while choice not in range(1, 3):
        try:
            choice = int(input(
                "Do you want to (1) pick a letter, or (2) guess the word: "
            ))
        except ValueError:
            print('Pick a valid choice!')
    if choice == 1:
        _pick_letter()
    else:
        _guess_phrase()


def _pick_letter():
    """Manage letter choice."""
    letter = ""
    while(letter not in ascii_uppercase or
          len(letter) != 1 or
          letter in game.chosen
          ):
        letter = input('Guess a letter: ').upper()
        if letter not in ascii_uppercase:
            letter = ""
            print('That is not a letter.')
        elif len(letter) != 1:
            letter = ""
            print('Enter a single letter.')
        elif letter in game.chosen:
            letter = ""
            print('You have already chosen that letter.')

    game.chosen.append(letter)

    if letter in game.word:
        count = 0
        update_word = ""
        for char in game.word:
            if char == letter:
                count += 1
                update_word += char
            elif char in game.chosen:
                update_word += char
            elif char not in ascii_uppercase:
                update_word += char
            else:
                update_word += PLACEHOLDER
        game.masked = update_word
        print(f'\nThere are {count} {letter}s in the word.\n')
        if game.masked == game.word:
            print("You have guessed all the letters.")
            print(game.word)
            game.win = True
    else:
        print(f'\nThere are no {letter}s in the word.\n')
        game.guess += 1
    return


def _guess_phrase():
    """Allow the user to guess the word."""
    guess = input("What is the secret word/phrase: ").upper()
    if guess == game.word:
        print("Correct!")
        game.win = True
    else:
        print("That is not the correct answer.")
        game.guess += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = ' '.join(sys.argv[1:])
    else:
        word = get_word()
    print(word)
    while validate_word(word):
        print('Picking another word.\n')
        word = get_word()

    game = Hangman(word)
    print("WELCOME TO HANGMAN")
    print("Here is your word/phrase:")
    print(game.masked)

    while game.guess < ALLOWED_GUESSES:
        get_user_guess()
        if game.win:
            print("You have avoided a gruesome death. Congrats.")
            break
        print(game)

    if not game.win:
        print('The hangman got you.')
        print(f'The correct answer was: {game.word}')

    sys.exit()
