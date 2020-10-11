from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class HangError(Exception):
    pass


class Hangman(object):
    def __init__(self, target: str):
        self.word = target
        self._word = target.lower()
        self._skeleton = [PLACEHOLDER if ch in ASCII else ch for ch in self._word]
        self.guesses = set()
        self.errors = 0

    def __str__(self):
        result = [HANG_GRAPHICS[self.errors], '', ' '.join(self.skeleton)]
        if len(self.guesses) > 0:
            result.append('Guessed: '+''.join(sorted(self.guesses)))
        return '\n'.join(result)

    @property
    def skeleton(self):
        return ''.join(self._skeleton)

    def _set_skeleton(self, index, value):
        self._skeleton[index] = value

    @property
    def finished(self):
        # Finished is indicated by the fact that the word and the skeleton have
        # become equal
        return self._word == self.skeleton

    def guess(self, ch: str):
        if ch not in ASCII:
            raise HangError(f'Invalid guess')
        if ch in self.guesses:
            raise HangError(f'{ch} already tried.')
        self.guesses.add(ch)
        if ch not in self._word:
            self.errors += 1
            if self.errors >= ALLOWED_GUESSES - 1:
                raise HangError('You\'re hanged!')
        else:
            idx = self._word.find(ch)
            while idx >= 0:
                self._set_skeleton(idx, ch)
                idx = self._word.find(ch, idx+1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()

    game = Hangman(word)

    while not game.finished:
        print(game)
        in_ch = input('Guess? ').lower()
        try:
            game.guess(in_ch)
        except HangError as e:
            if 'hanged' in e.args[0].lower():
                print(game)
                print('Oh dear, perhaps you weren\'t cut out for this.')
                print(f'You were trying to find the word: {game.word}')
                break
            if 'invalid' in e.args[0].lower():
                print('That is not a valid character')
                continue
            print('Whoops, try again.')
    else:
        print(game)
        print('Well done you won!')
