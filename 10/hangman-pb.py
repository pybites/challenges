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
        self.num_guesses = 0
        self.num_wrong_guesses = 0
        self.letters_used = set()

    def _guess_letter(self):
        """Interface to user to guess letter, ValueError if wrong input"""
        self.num_guesses += 1
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
        """Checks secret word for matches updating the guessed word list.
           Returns boolean if there were matches"""
        prev_state_guessed_word = list(self.guessed_word)
        for i, char in enumerate(self.secret_word):
            if letter == char:
                self.guessed_word[i] = letter
        return self.guessed_word != prev_state_guessed_word

    def _has_won(self):
        """If no placeholders left, we have a winner"""
        return PLACEHOLDER not in self.guessed_word

    def _show_hang_graph_and_status(self):
        """Prints status after bad guess"""
        print(HANG_GRAPHICS[self.num_wrong_guesses] + '\n')
        wrong_letters = ', '.join(self.letters_used - set(self.guessed_word))
        print('Wrong letters: {}'.format(wrong_letters))

    def __call__(self):
        """Entry point to the game, runs till 1. game is won (return), 2. lost game =
           number allowed guesses ran out"""
        while self.num_wrong_guesses < ALLOWED_GUESSES:
            if DEBUG:
                print(self)
            print(' '.join(self.guessed_word))
            try:
                letter = self._guess_letter()
            except ValueError as exc:
                print(exc)
                continue
            good_turn = self._update_guess_with_letter(letter)
            if self._has_won():
                guessed_word = ''.join(self.guessed_word)
                print('\nYou won! You guessed {} in {} guesses :)'.format(
                    guessed_word, self.num_guesses))
                return
            if not good_turn:
                self._show_hang_graph_and_status()
                self.num_wrong_guesses += 1
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
    Hangman(word)()
