from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, word):
        self.word = word
        self.guess = [PLACEHOLDER if letter != ' ' else ' ' for letter in word]
        self.guesses_remaining = ALLOWED_GUESSES
        self.guesses = None
        self.available_letters = ASCII
        self.letters_guessed = []

    def make_guess(self, letter):
        """Makes a guess at the word."""
        self.letters_guessed.append(letter)
        self.available_letters.remove(letter)

        if letter not in self.word.lower():
            if self.guesses is None:
                self.guesses = 0
            else:
                self.guesses += 1

            self.guesses_remaining -= 1

            print(f'Oops! That guess was incorrect! {self.guesses_remaining} guesses left.')
            return

        for i, char in enumerate(self.word.lower()):
            if letter == char:
                self.guess[i] = letter

    def __str__(self):
        current_word = ' '.join(self.guess)

        if self.guesses is None:
            return f"""
    {current_word}

    Letters guessed: {', '.join(sorted(self.letters_guessed))}"""

    #     if self.guesses_remaining == ALLOWED_GUESSES:
    #         return f"""
    # {current_word}

    # Letters guessed: {', '.join(sorted(self.letters_guessed))}"""

    #     if self.guesses_remaining == ALLOWED_GUESSES:
    #         return f"""
        # ________      
        # |            
        # |             
        # |             
        # |             
        # |

    # # {current_word}

    # # Letters guessed: {', '.join(sorted(self.letters_guessed))}"""

        return f"""{HANG_GRAPHICS[self.guesses]}

    {current_word}

    Letters guessed: {', '.join(sorted(self.letters_guessed))}"""
    #     return f"""{HANG_GRAPHICS[ALLOWED_GUESSES - self.guesses_remaining]}

    # {current_word}

    # Letters guessed: {', '.join(sorted(self.letters_guessed))}"""


def main():
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()

    punc = "',?."
    for char in punc:
        if char in word:
            word.replace(char, '')

    hangman = Hangman(word)

    while True:
        print(f'{hangman}\n')

        if not hangman.guesses_remaining:
            print(f'Game over! The movie was {word}')
            break

        if ''.join(hangman.guess).replace(' ', '') == hangman.word.replace(' ', '').lower():
            print(f'You won! The movie was {word}')
            break

        letter = input('Choose a letter: ').lower()

        if letter not in hangman.available_letters:
            print('You already guessed that letter. Try again.')
            continue

        if letter not in ASCII:
            print('That is not a valid letter. Try again.')
            continue

        hangman.make_guess(letter)


if __name__ == '__main__':
    main()
