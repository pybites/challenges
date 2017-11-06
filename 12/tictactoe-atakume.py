from operator import itemgetter
import os
import random

DEFAULT = '_'
VALID_POSITIONS = list(range(1, 10))
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)
PLAYER_X = "X"
PLAYER_O = "O"
AUTO_PLAYER = PLAYER_O

DRAW_GAME = 20

class TicTacToe:

    def __init__(self, mode='multiplayer'):
        self.board = [None] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0
        self.turns = 0
        self.player = PLAYER_X
        self.mode = mode

    def __str__(self):
        os.system('clear')
        result = ""
        for i in range(1, len(self.board), 3):
            result += " ".join(self.board[i: i + 3]) + "\n"
        return result

    def is_win(self):
        return self.player if TicTacToe.player_wins(self.player, self.board) else None

    def is_end(self):
        return TicTacToe.is_draw(self.board)

    def take_turn(self):
        if self.mode == 's' and self.player == AUTO_PLAYER:
            move = self.compute_move()
        else:
            move = input("Take turn: ")
            while not self.proper_move(move):
                move = input("Wrong move try again: ")
        self.make_move(move)

    def proper_move(self, move):
        return move.isdigit() and int(move) in TicTacToe.available_steps(self.board)

    def make_move(self, move):
        self.board[int(move)] = self.player
        self.turns += 1

    def compute_move(self):
        return next(TicTacToe.available_steps(self.board), None)

    def next_turn(self):
        self.player = PLAYER_O if self.player == PLAYER_X else PLAYER_X

    @staticmethod
    def available_steps(board):
        return [i for i in VALID_POSITIONS if board[i] == DEFAULT]

    @staticmethod
    def player_wins(player, board):
        return any(all(player == i for i in itemgetter(a, b, c)(board)) for a, b, c in WINNING_COMBINATIONS)

    @staticmethod
    def is_draw(board):
        return len(TicTacToe.available_steps(board)) == 0


class RandomAITicTacToe(TicTacToe):
    def compute_move(self):
        return random.choice(TicTacToe.available_steps(self.board))


class MinMaxAITicTacToe(TicTacToe):
    def __init__(self, mode='multiplayer'):
        super(MinMaxAITicTacToe, self).__init__(mode)
        self.choice = 0

    def compute_move(self):
        self.minmax(self.board, 0)
        return self.choice

    def minmax(self, board, depth):
        self.choice

        depth += 1
        scores = []
        steps = []

        def update_state(board, step, depth):
            board = list(board)
            board[step] = PLAYER_X if depth % 2 else PLAYER_O
            return board

        def unit_score(winner, depth):
            if winner == DRAW_GAME:
                return 0
            else:
                return 10 - depth if winner == PLAYER_X else depth - 10

        def check_win_game(board):
            for player in [PLAYER_X, PLAYER_O]:
                if TicTacToe.player_wins(player, board):
                    return player
            return DRAW_GAME if TicTacToe.is_draw(board) else 10

        result = check_win_game(board)
        if result != 10:
            return unit_score(result, depth)

        for step in TicTacToe.available_steps(board):
            score = self.minmax(update_state(board, step, depth), depth)
            scores.append(score)
            steps.append(step)

        if depth % 2 == 1:
            max_value_index = scores.index(max(scores))
            self.choice = steps[max_value_index]
            return max(scores)
        else:
            min_value_index = scores.index(min(scores))
            self.choice = steps[min_value_index]
            return min(scores)

if __name__ == "__main__":
    another = "y"
    while True:
        player_mode = input("For singleplayer mode type 's': ")
        game = MinMaxAITicTacToe(player_mode)
        print(game)
        while not game.is_end():
            game.take_turn()
            print(game)
            if game.is_win():
                break
            game.next_turn()

        another = input("Game over. Play once again?")
        if another.lower() not in ["y", "yes"]:
            break
