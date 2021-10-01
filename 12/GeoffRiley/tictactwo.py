"""
    Proper name: 'Naughts and Crosses'
    Irish name: 'Xs and Os'
    American name: 'Tic Tac Toe'
    Reason: Who on Earth has a clue?  It's an historical thing.
"""
from itertools import cycle
from typing import List, Union, Set, Tuple, Iterator

# External representations of the playing symbols
BLANK_SYM: str = '_'
O_SYM: str = 'O'
X_SYM: str = 'X'
# Internal representations of the playing symbols
BLANK_VALUE: int = 0
O_VALUE: int = 1
X_VALUE: int = 2
# Translation between systems
VAL_TO_SYM: dict = {
    BLANK_VALUE: BLANK_SYM,
    O_VALUE: O_SYM,
    X_VALUE: X_SYM,
}
SYM_TO_VAL: dict = {
    BLANK_SYM: BLANK_VALUE,
    O_SYM: O_VALUE,
    X_SYM: X_VALUE,
}
OPPONENT: dict = {
    O_VALUE: X_VALUE,
    X_VALUE: O_VALUE,
}
INTERNAL_TO_EXTERNAL: dict = {
    0: 7, 1: 8, 2: 9,
    3: 4, 4: 5, 5: 6,
    6: 1, 7: 2, 8: 3
}
EXTERNAL_TO_INTERNAL: dict = {
    7: 0, 8: 1, 9: 2,
    4: 3, 5: 4, 6: 5,
    1: 6, 2: 7, 3: 8
}
VALID_POSITIONS: Set[int] = set(range(1, 10))
# A winning combination exists for three symbols in a row:
WINNING_COMBINATIONS: List[Tuple[int, int, int]] = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


class BlockedCell(Exception):
    pass


class InvalidMove(Exception):
    pass


class TicTacToe:
    # define the types of various internal variables
    _board: List[int]
    _turn: int
    _turn_cycle: Iterator[int]
    _move: int

    def __init__(self):
        """Constructor, allocate the blank board"""
        # Create an array of cells to hold the grid positions.
        self._board = [BLANK_VALUE] * len(VALID_POSITIONS)
        self._turn_cycle = cycle([O_VALUE, X_VALUE])
        self._turn = self._next_turn()
        self._move = 0

    def _next_turn(self) -> int:
        return next(self._turn_cycle)

    def __str__(self):
        """Print the board"""
        return '\n'.join(
            ' '.join(
                VAL_TO_SYM[c]
                for c in self._board[s * 3:(s + 1) * 3]
            ) for s in range(3)
        )

    @staticmethod
    def _ndx_to_cell_(ndx: int) -> int:
        return EXTERNAL_TO_INTERNAL[ndx]

    @staticmethod
    def _cell_to_ndx_(cell: int) -> int:
        return INTERNAL_TO_EXTERNAL[cell]

    def player_move(self, target_position: int):
        """
        Attempt to place the player move

        May raise exceptions: BlockCell, InvalidMove
        """
        if target_position in VALID_POSITIONS:
            cell = self._ndx_to_cell_(target_position)
            if self._board[cell] is BLANK_VALUE:
                self._board[cell] = self._turn
            else:
                raise BlockedCell(
                    f'Cannot play at {target_position}, it is already held by {VAL_TO_SYM[self._board[cell]]}')
        else:
            raise InvalidMove(f'Invalid move, {target_position} not available')

    def next_player(self) -> str:
        self._turn = self._next_turn()
        return VAL_TO_SYM[self._turn]

    def find_winner(self) -> Union[int, None]:
        """Find a winner, 'O', 'X' or None"""
        for s in [O_VALUE, X_VALUE]:
            if any(all(self._board[c] == s for c in combo) for combo in WINNING_COMBINATIONS):
                return s
        return None

    @property
    def win(self) -> bool:
        """Test if the game is won"""
        return self.find_winner() == self._turn

    @property
    def lose(self) -> bool:
        """Test if the game is lost"""
        return self.find_winner() == OPPONENT[self._turn]

    @property
    def draw(self) -> bool:
        """Test if the game is a draw"""
        return not (any(c == BLANK_VALUE for c in self._board))

    @property
    def win_draw_lose(self) -> bool:
        """Test if the game is still in play"""
        return self.win or self.lose or self.draw

    @property
    def player(self) -> str:
        return VAL_TO_SYM[self._turn]


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        print("Let's play Naughts and Crosses!")
        while not game.win_draw_lose:
            print('\nCurrent state of game:')
            print(game)
            try:
                mv = input(f'Where would you like to play your {game.player}? ')
                position = int(mv)
                game.player_move(position)
                if game.win:
                    print(game)
                    print(f'**WIN** We have a WINNER!!  Well done {game.player}.')
                    break
                if game.draw:
                    print(game)
                    print('**DRAW** That was a little pointless in the end.')
                    break
                game.next_player()
            except InvalidMove:
                print(f'Poor choice, Grasshopper, "{mv}" is not and acceptable move: use the numeric keypad layout!')
            except BlockedCell:
                print(f'Sorry that spot is already taken.')
            except ValueError:
                print(f'Please indicate position as though it were the numeric keypad.')
