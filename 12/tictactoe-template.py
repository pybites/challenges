DEFAULT = '_'  # or ' '
VALID_POSITIONS = list(range(1, 10))  # could number board: 7-8-9, 4-5-6, 1-2-3
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)


class TicTacToe:

    def __init__(self):
        '''Constructor, below worked well for us ...'''
        self.board = [None] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0

    def __str__(self):
        '''Print the board'''
        pass

    # TODOS:
    # display board in __str__ (clearing screen)
    # have at least an is_win method to exit game
    # num turns = len(VALID_POSITIONS) so might not need is_draw (tie) method
    # have method(s) to get user input and validate
    # if playing against computer (AI) calculate next best move (algorithm)
    # update board upon each turn


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        # take turn
        # make move
        # check win - break
        #
        # ask if another game, if n - break
