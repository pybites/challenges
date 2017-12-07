'''Simple tictactoe game, board positions are like keyboard
                7 8 9
                4 5 6
                1 2 3
'''

from builtins import input
from collections import Counter
from functools import wraps
import itertools
import os
import sys

DEFAULT = '_'
VALID_POSITIONS = list(range(1, 10))
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)
POSITION_VALUES = Counter(
    itertools.chain(*WINNING_COMBINATIONS)
)
PLAYER = 'O'
COMPUTER = 'X'


def clear_screen(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        os.system('cls' if os.name == 'nt' else 'clear')
        r = f(*args, **kwargs)
        return r
    return wrapped


class TicTacToe:

    def __init__(self):
        self.board = [None] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0

    @clear_screen
    def __str__(self):
        return '''
            {} | {} | {}
            {} | {} | {}
            {} | {} | {}
        '''.format(*(self.board[7:] + self.board[4:7] + self.board[1:4]))

    def is_win(self):
        for combo in WINNING_COMBINATIONS:
            a, b, c = combo
            combo_vals = set([self.board[a], self.board[b], self.board[c]])
            if DEFAULT not in combo_vals and len(combo_vals) == 1:
                return True
        return False

    def _get_pos(self):
        while True:
            try:
                pos = int(input('Next move: '))
                return pos
            except ValueError:
                print('Numeric value please')
                continue

    def _validate(self, pos):
        if pos not in VALID_POSITIONS:
            print('Not in valid position range: {}'.format(VALID_POSITIONS))
            return False
        if self.board[pos] != DEFAULT:
            print('Position already taken by a previous move')
            return False
        return True

    def _update_board(self, combo, combo_vals):
        index = combo_vals.index(DEFAULT)
        empty_slot = combo[index]
        self.board[empty_slot] = COMPUTER
        return True

    def _win_or_block(self):
        for combo in WINNING_COMBINATIONS:
            a, b, c = combo
            combo_vals = [self.board[a], self.board[b], self.board[c]]
            # can only use unitiated positions
            if DEFAULT not in combo_vals:
                continue
            if combo_vals.count(COMPUTER) == 2:
                return self._update_board(combo, combo_vals)
            if combo_vals.count(PLAYER) == 2:
                return self._update_board(combo, combo_vals)
        return False

    def _take_best_next_free_pos(self):
        for pos, _ in POSITION_VALUES.most_common():
            if self.board[pos] == DEFAULT:
                self.board[pos] = COMPUTER
                return True
        return False

    def ai_move(self):
        self._win_or_block() or self._take_best_next_free_pos()

    def manual_move(self):
        pos = self._get_pos()
        valid = self._validate(pos)
        if not valid:
            self.manual_move()
        else:
            self.board[pos] = PLAYER


if __name__ == "__main__":
    if 'hard' in ''.join(sys.argv[1:]).lower():
        first, second = COMPUTER, PLAYER
    else:
        first, second = PLAYER, COMPUTER

    while True:
        game = TicTacToe()

        turns = itertools.cycle([first, second])
        print(game)
        for _ in VALID_POSITIONS:
            player = next(turns)
            if player == COMPUTER:
                game.ai_move()
            else:
                game.manual_move()
            print(game)
            if game.is_win():
                print('Player {} wins'.format(player))
                break
        else:  # for / else is frowned upon, I do like it here though!
            print('Draw')

        if 'n' in input('Do you want to play again? [yn] ').lower():
            print('Goodbye')
            break
