"""
    Proper name: 'Naughts and Crosses'
    American name: 'Tic Tac Toe'
    Reason: Who on Earth has a clue?
"""

# Definition of game elements
# Working with a 3 x 3 grid represented as a linear array of nine cells
# initialise to `DEFAULT`
from typing import List

DEFAULT: str = '_'
# Visualise the board cells numbered as:
#  7  8  9
#  4  5  6
#  1  2  3
# (Just like a numeric keypad!)
VALID_POSITIONS: List[int] = list(range(1, 10))
# A winning combination exists for three symbols in a row:
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)


class TicTacToe:
    _board: List[str]

    def __init__(self):
        """Constructor, allocate the blank board"""
        # Create an array of cells to hold the grid positions.
        self._board = [DEFAULT] * len(VALID_POSITIONS)
        self._turn = 'O'
        self._move = 0

    def __str__(self):
        """Print the board"""
        return '\n'.join(''.join(c for c in self._board[s * 3:(s + 1) * 3]) for s in range(3))

    @staticmethod
    def _ndx_to_cell_(ndx: int) -> int:
        return {7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8}[ndx]

    @staticmethod
    def _cell_to_ndx_(cell: int) -> int:
        return {0: 7, 1: 8, 2: 9, 3: 4, 4: 5, 5: 6, 6: 1, 7: 2, 8: 3}[cell]

    # TODOS:
    # display board in __str__ (clearing screen)
    # have at least an is_win method to exit game
    # num turns = len(VALID_POSITIONS) so might not need is_draw (tie) method
    # have method(s) to get user input and validate
    # if playing against computer (AI) calculate next best move (algorithm)
    # update board upon each turn
    def player_move(self, position: int):
        pass


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        # take turn
        # make move
        # check win - break
        #
        # ask if another game, if n - break
