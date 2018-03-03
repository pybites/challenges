from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
DEBUG = False
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    """A simple hangman game"""

    def __init__(self, word=None):
        """Setup: get word or pick random one, set a placeholders list,
           ascii only, skip (display) punctuation, init state vars"""
        if word is None:
            word = get_word()
        self.secret_word = list(word.lower())
        self.guessed_word = [PLACEHOLDER if c in ASCII else c
                             for c in self.secret_word]
        # status variables
        self.num_guesses = 0
        self.num_wrong_guesses = 0
        self.letters_used = set()
        self.wrong_letters = set()

    def _guess_letter(self):
        """Gets letter from user and validates it."""
        letter = input('\nGuess #{}: enter letter: '.format(self.num_guesses))
        letter = letter.lower()
        if letter not in ASCII:
            raise ValueError('Not a valid letter, try again')
        elif letter in self.letters_used:
            raise ValueError('Letter already used, try again')
        else:
            self.letters_used.add(letter)
            return letter

    def _update_guess_with_letter(self, letter):
        """Updates guessed word with guess letter if in secret word."""
        for i, char in enumerate(self.secret_word):
            if letter == char:
                self.guessed_word[i] = letter

    def _has_won(self):
        """If no placeholders chars left in guessed word == win"""
        return PLACEHOLDER not in self.guessed_word

    def _show_guessed_word(self):
        print(' '.join(self.guessed_word))

    def _show_status(self):
        """Prints status graph and information"""
        if DEBUG:
            print('\n---Debug---\n{}\n---\n'.format(self))
        if self.num_wrong_guesses > 0:
            print(HANG_GRAPHICS[self.num_wrong_guesses - 1] + '\n')
        if self.wrong_letters:
            print('Guessed letters not in word: {}'.format(
                ', '.join(self.wrong_letters)))

    def play(self):
        """Entry point to the game, results in win or loss"""
        while self.num_wrong_guesses < ALLOWED_GUESSES:
            self._show_guessed_word()

            try:
                self.num_guesses += 1
                letter = self._guess_letter()
            except ValueError as exc:
                print(exc)
                self.num_guesses -= 1
                continue

            if letter in self.secret_word:
                self._update_guess_with_letter(letter)
            else:
                self.wrong_letters.add(letter)
                self.num_wrong_guesses += 1

            if self._has_won():
                print('\nYou won! You guessed {} in {} guesses :)'.format(
                    ''.join(self.guessed_word), self.num_guesses))
                return

            self._show_status()

        print('\nGame over :(')
        print('The word was: {}'.format(''.join(self.secret_word)))

    def __str__(self):
        """String representation, easy to dump secret vs guess for debugging"""
        out = []
        for k, v in self.__dict__.items():
            v = ''.join(v) if isinstance(v, list) else v
            out.append('{:<15}: {}'.format(k, v))
        return '\n'.join(out)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = None
    hangman = Hangman(word)
    hangman.play()
