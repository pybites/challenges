from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


with open('records.txt', 'r') as fp:
    previous_record = int(fp.readlines()[-1])


class Hangman(object):
    def __init__(self, movie):
        self.movie = movie
        self._num_guesses = 0
        self._wrong_guesses = 0
        self._movie = [PLACEHOLDER if letter in ASCII else letter for letter in self.movie]
        self._guessed = set()
        self._guessed_wrong = set()

    def _guess_letter(self):
        letter = input(f'Guess #{self._num_guesses}: Enter letter: ')
        if letter not in ASCII:
            raise ValueError('Enter a valid letter (a to z) or (A to Z), try again')
        elif letter in self._guessed or letter in self._guessed_wrong:
            raise ValueError('Letter already guessed, try again')
        else:
            return letter

    def _check_letter(self, letter):
        if letter in self.movie:
            self._guessed.add(letter)
            for index, c in enumerate(self.movie):
                if c == letter:
                    self._movie[index] = letter
        else:
            self._guessed_wrong.add(letter)
            self._wrong_guesses = len(self._guessed_wrong)

    def _show_status(self):
        if PLACEHOLDER not in self._movie:
            print(f'Hurray!, you have won!!!. You have correctly guessed the movie "{self.movie}" '
                  f'in {self._num_guesses} guesses')
            exit(0)
        if self._wrong_guesses > 0:
            print(HANG_GRAPHICS[self._wrong_guesses - 1])
        if self._guessed_wrong:
            print(f'\nWrongly guessed letters: {", ".join(self._guessed_wrong)}')

    def start(self):
        while self._wrong_guesses < ALLOWED_GUESSES:
            print(' '.join(self._movie))
            print()
            try:
                self._num_guesses += 1
                letter = self._guess_letter()
            except ValueError as v:
                print(v)
                self._num_guesses -= 1
                continue

            self._check_letter(letter)
            self._show_status()
        print(f'Game over, you have used all your guesses!!. The movie is "{self.movie}"')


def _guess_letter():
    letter = input(f'Guess #{_num_guesses}: Enter letter: ')
    if letter not in ASCII:
        raise ValueError('Enter a valid letter (a to z) or (A to Z), try again')
    elif letter in _guessed or letter in _guessed_wrong:
        raise ValueError('Letter already guessed, try again')
    else:
        return letter


def _check_letter(letter):
    if letter in movie:
        _guessed.add(letter)
        for index, c in enumerate(movie):
            if c == letter:
                _movie[index] = letter
    else:
        global _wrong_guesses
        _guessed_wrong.add(letter)
        _wrong_guesses = len(_guessed_wrong)


def _show_status():
    if PLACEHOLDER not in _movie:
        if _num_guesses < previous_record:
            print(f'Its a new record!!. Your previous record was {previous_record} guesses')
        print(f'Hurray!, you have won!!!. You have correctly guessed the movie "{movie}" '
              f'in {_num_guesses} guesses')
        with open('records.txt', 'a') as fp:
            fp.write('\n')
            fp.write(f'{_num_guesses}')
        exit(0)
    if _wrong_guesses > 0:
        print(HANG_GRAPHICS[_wrong_guesses - 1])
    if _guessed_wrong:
        print(f'\nWrongly guessed letters: {", ".join(_guessed_wrong)}')


def start():
    global _num_guesses
    while _wrong_guesses < ALLOWED_GUESSES:
        print(' '.join(_movie))
        print()
        try:
            _num_guesses += 1
            letter = _guess_letter()
        except ValueError as v:
            print(v)
            _num_guesses -= 1
            continue

        _check_letter(letter)
        _show_status()
    print(f'Game over, you have used all your guesses!!. The movie is "{movie}"')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        movie = sys.argv[1]
    else:
        movie = get_word().lower()
    _num_guesses = 0
    _wrong_guesses = 0
    _movie = [PLACEHOLDER if letter in ASCII else letter for letter in movie]
    _guessed = set()
    _guessed_wrong = set()

    start()
