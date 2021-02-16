"""
    Proper name: 'Naughts and Crosses'
    American name: 'Tic Tac Toe'
    Reason: Who on Earth has a clue?
"""
from collections import defaultdict
from functools import reduce
from itertools import cycle
from operator import mul
from typing import List, Union, Set, Tuple, Iterator

# Definition of game elements
# External representation of grid is numbered 1 to 9;
# internal representation of grid is numbered 0 to 8.
# Working with a 3 x 3 grid represented as a linear array of nine cells
# initialise to `DEFAULT`
BLANK_SYM: str = '_'
O_SYM: str = 'O'
X_SYM: str = 'X'
BLANK_VALUE: int = 2
O_VALUE: int = 3
X_VALUE: int = 5
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
# Visualise the board cells numbered as:
#  Internal   External
#  0  1  2    7  8  9
#  3  4  5    4  5  6
#  6  7  8    1  2  3
#             (Just like a numeric keypad!)
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
    (6, 7, 8), (3, 4, 5), (0, 1, 2),
    (6, 3, 0), (7, 4, 1), (8, 5, 2),
    (0, 4, 8), (6, 4, 2),
]
# The product of values in an *almost* winning line…
WINNING_PROD = {
    O_VALUE: 18,
    X_VALUE: 50,
}


class BlockedCell(Exception):
    pass


class InvalidMove(Exception):
    pass


class TicTacToe:
    # define the types of various internal variables
    _board: List[int]
    _turn_cycle: Iterator[int]
    _turn: int
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
        return ' ' + '\n---+---+---\n '.join(
            ' | '.join(VAL_TO_SYM[c]
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

    def ai_move(self) -> str:
        return str(self._cell_to_ndx_(self._ai_move()))

    def _ai_move(self) -> int:
        """Work out a move for the computer"""
        # Working from the Strategy presented on Wikipedia
        #       [https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy]
        # 1. Win: If the player has two in a row, they can place a
        #       third to get three in a row.
        #
        # Using 3 and 5 for 'O' and 'X' and 2 for empty means that
        # in order to identify a 'winning' line we can take the
        # product of the values to work out what if an appropriate
        # gap is present.
        # (Distinct) Possible products are:
        #   _ _ _ → 2 x 2 x 2 = 8
        #   O _ _ → 3 x 2 x 2 = 12
        #   O O _ → 3 x 3 x 2 = 18 [Winning O line]
        #   O O O → 3 x 3 x 3 = 27
        #   O X _ → 3 x 5 x 2 = 30
        #   O O X → 3 x 3 x 5 = 45
        #   X _ _ → 5 x 2 x 2 = 20
        #   X X _ → 5 x 5 x 2 = 50 [Winning X line]
        #   X X X → 5 x 5 x 5 = 125
        #   X X O → 5 x 5 x 3 = 75
        # Therefore it can be seen that there is a single value
        # indicating a winning line for either Os or Xs
        winning_lines = defaultdict(set)
        for line in WINNING_COMBINATIONS:
            prod = reduce(mul, [self._board[c] for c in line])
            winning_lines[prod].add(line)

        # Let's see if there is a winning line for the current player
        if winning_lines[WINNING_PROD[self._turn]]:
            # find the blank in the first winning line.
            line = winning_lines[WINNING_PROD[self._turn]].pop()
            return [n for n in line if self._board[n] == BLANK_VALUE][0]

        # 2. Block: If the opponent has two in a row, the player
        #       must play the third themselves to block the opponent.
        if winning_lines[WINNING_PROD[OPPONENT[self._turn]]]:
            # find the blank to play a block.
            line = winning_lines[WINNING_PROD[OPPONENT[self._turn]]].pop()
            return [n for n in line if self._board[n] == BLANK_VALUE][0]

        # 3. Fork: Create an opportunity where the player has two
        #       ways to win (two non-blocked lines of 2).

        # 4. Blocking an opponent's fork:
        #       If there is only one possible fork for the opponent,
        #       the player should block it.
        #       Otherwise, the player should block all forks in any
        #       way that simultaneously allows them to create two
        #       in a row.
        #       Otherwise, the player should create a two in a row
        #       to force the opponent into defending, as long as it
        #       doesn't result in them creating a fork.
        #       For example, if "X" has two opposite corners and
        #       "O" has the center, "O" must not play a corner move
        #       in order to win. (Playing a corner move in this
        #       scenario creates a fork for "X" to win.)

        # 5. Center: A player marks the center. (If it is the first
        #       move of the game, playing a corner move gives the
        #       second player more opportunities to make a mistake
        #       and may therefore be the better choice; however, it
        #       makes no difference between perfect players.)
        if self._board[4] == BLANK_VALUE:
            return 4

        # 6. Opposite corner: If the opponent is in the corner, the
        #       player plays the opposite corner.
        for x, y in [(0, 8), (2, 6), (6, 2), (8, 0)]:
            if self._board[x] == OPPONENT[self._turn] and self._board[y] == BLANK_VALUE:
                return y

        # 7. Empty corner: The player plays in a corner square.
        for x in [0, 2, 6, 8]:
            if self._board[x] == BLANK_VALUE:
                return x

        # 8. Empty side: The player plays in a middle square on any
        #       of the 4 sides.
        for x in [1, 3, 5, 7]:
            if self._board[x] == BLANK_VALUE:
                return x

        raise InvalidMove(f"Couldn't identify a move to make for AI controlled {self.player}")


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        print("Let's play Naughts and Crosses!")
        while not game.win_draw_lose:
            print('\nCurrent state of game:')
            print(game)
            try:
                if game.player == 'O':
                    mv = input(f'Where would you like to play your {game.player}? ')
                else:
                    mv = game.ai_move()
                    print(f'\nComputer chooses to play {game.player} at {mv}.')
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
            except InvalidMove as exc:
                print(f'Poor choice, Grasshopper, "{mv}" is not and acceptable move: use the numeric keypad layout!')
                print(f'DEBUG: {exc}')
            except BlockedCell as exc:
                print(f'Sorry that spot is already taken.')
                print(f'DEBUG: {exc}')
            except ValueError as exc:
                print(f'Please indicate position as though it were the numeric keypad.')
                print(f'DEBUG: {exc}')
