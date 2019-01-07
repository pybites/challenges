from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class SecretWord:
    def __init__(self, word):
        self.secret = [PLACEHOLDER if char.lower() in ASCII else char for char in word]
        self.open = word

    def __repr__(self):
        return self.secret

    def open_letter(self, letter):
        for index, char in enumerate(self.open):
            if letter == char.lower():
                self.secret[index] = self.open[index]


class Hangman:
    def __init__(self, word):
        self.word = SecretWord(word.strip())
        self.tries_left = ALLOWED_GUESSES
        self.hang_graphics = hang_graphics()
        self.guessed_letters = []
        self.exit = 'exit'

    def play(self):
        while PLACEHOLDER in self.word.secret and self.tries_left:
            self._print_secret()
            letter = self._get_letter()
            if letter == self.exit:
                return

            if not letter or letter in self.guessed_letters:
                continue

            if letter in self.word.open.lower():
                self.word.open_letter(letter)
                self.guessed_letters += [letter]
            else:
                self.tries_left -= 1
                print(next(self.hang_graphics), end='\n\n')
                self.guessed_letters += [letter]

    def print_result(self):
        if PLACEHOLDER not in self.word.secret:
            print('You win!')
            print('Word: ', self.word.open)
        else:
            print('You lose')
            print('Word: ', self.word.open)

    def _print_secret(self):
        print(*self.word.secret, end='\n\n')

    def _get_letter(self):
        letter = input('input letter: ').lower()
        if letter in ASCII and len(letter) == 1 or letter == self.exit:
            return letter


if __name__ == '__main__':
    word = sys.argv[1] if len(sys.argv) > 1 else get_word()
    hangman = Hangman(word)
    hangman.play()
    hangman.print_result()
