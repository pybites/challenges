from enum import Enum
import random

DEFAULT = '_'  # or ' '
VALID_POSITIONS = list(range(1, 10))  # could number board: 7-8-9, 4-5-6, 1-2-3
WINNING_COMBINATIONS = (
    (7, 8, 9), (4, 5, 6), (1, 2, 3),
    (7, 4, 1), (8, 5, 2), (9, 6, 3),
    (1, 5, 9), (7, 5, 3),
)

class TicTacToe:

    Mode = Enum('Mode', {'HUMAN' : 'human', 'COMPUTER' : 'computer'})

    # Initializes board
    def __init__(self):
        self.init_board()
        self.ask_game_mode()
        self._num_turns = 0
        # A value of 0 indicates that the first player goes first.
        # A value of 1 indicates that the second player, whether a human or the computer, 
        # should go second.
        self._starting_player = random.randrange(2)

        print('*' * 20)

        if self.mode == self.Mode.HUMAN:
            print(f'Welcome to Tic-Tac-Toe! This match will be human v. {self.mode.value}')
            print(f'The starting player will be human {self._starting_player + 1}')
        else:
            print(f'Welcome to Tic-Tac-Toe! This match will be human v. {self.mode.value}')
            print('The starting player will be the '
                 f'{"human" if self._starting_player == 0 else "computer"}')

        print('*' * 20)

    def init_board(self):
        self.board = [None] + len(VALID_POSITIONS) * [DEFAULT]  # skip index 0

    # Asks user for game mode, either against another human or against a computer
    def ask_game_mode(self):
        print("Would you like to play against another human or against the computer? (h/c) ")
        choice = input().strip().lower()
        while choice not in ('h', 'c'):
            print("Please enter a valid string")
            print("Would you like to play against another human or against the computer? (h/c) ")
            choice = input().strip().lower()
        
        self.mode = self.Mode.HUMAN if choice == 'h' else self.Mode.COMPUTER


    # Will print the board out as a 3x3 array of Xs, Os, and _s
    def __str__(self):
        
        result = '\nBoard\n'
        result += '\n'.join(' '.join(self.board[(3 * i) + 1 : (3 * i) + 4]) for i in range(3))

        return result


    def is_done(self):
        if self._num_turns == 9:
            print('\nA draw has occurred')
            return True
        elif self._is_win() != 0:
            if self._is_win() == 1:
                print('The first player won! Congrats!')
            # Win code == 2, player 2 won
            elif self.mode == self.Mode.HUMAN:
                print('The second player won, congrats!')
            else:
                print('The computer won, better luck next time!')
            return True
        
        return False

    # Checks if the game is won yet.
    def _is_win(self) -> int:
        for combo in WINNING_COMBINATIONS:
            if all(self.board[i] == 'O' for i in combo):
                return 1
            elif all(self.board[i] == 'X' for i in combo):
                return 2
        return 0

    def next_turn(self):
        print(self)

        if self._starting_player == self._num_turns % 2:
            self._turn('O')
        else:
            if self.mode == self.Mode.HUMAN:
                self._turn('X')
            else:
                # Computer will always have token 'X'
                print('\nComputer\'s turn:')
                self._computer_turn()

        self._num_turns += 1

    def _turn(self, token : str) -> int:
        print(f'\nYour play token is \'{token}\', enter the number of an empty spot in the board '
              f'to place an \'{token}\' there.')

        while True:
            try:
                placement = int(input().strip())
            except TypeError:
                print('Please enter an integer value')
            # If an int value, now check if it can be placed into board
            else:
                try:
                    self._mutate_board(token, placement)
                    break
                except ValueError:
                    print('Please enter an integer value from 1-9 for a place in the board that\'s empty')


    # Checks if chosen spot in board is empty. If so, places token. If not, error raised in
    # the calling function
    def _mutate_board(self, token : str, placement : int):
        if placement in range(1, 10) and self.board[placement] == DEFAULT:
            self.board[placement] = token
        else:
            raise ValueError
    
    # Computer will always have 'X' token
    # Consulted https://en.wikipedia.org/wiki/Tic-tac-toe
    def _computer_turn(self):
        MY_TOKEN = 'X'
        OPP_TOKEN = 'O'

        # Introduce some randomness so computer doesn't always win
        if random.choice((0, 1)) == 0:
            empty_places = [place for place in range(1, 10) if self.board[place] == DEFAULT]
            self.board[random.choice(empty_places)] = MY_TOKEN
            return

        # 1. Win
        # Does winning move if possible
        for placement in range(1, 10):
            if self.board[placement] == DEFAULT:
                self.board[placement] = MY_TOKEN
                if self._is_win():
                    return
                else:
                    self.board[placement] = DEFAULT

        # 2. Block
        # Blocks opponent's possibly winning move
        for placement in range(1, 10):
            if self.board[placement] == DEFAULT:
                self.board[placement] = OPP_TOKEN
                if self._is_win():
                    self.board[placement] = MY_TOKEN
                    return
                else:
                    self.board[placement] = DEFAULT

        # There must be two possible threats in order to create a fork
        def _fork_exists(token: str, placement : int) -> bool:
            threats = 0

            for combo in WINNING_COMBINATIONS:

                my_token_placements = 0
                empty_placements = 0

                for num in combo:
                    if self.board[num] == token:
                        my_token_placements += 1
                    elif self.board[num] == DEFAULT:
                        empty_placements += 1

                # Check that at least two of the tokens 
                threat_exists = my_token_placements == 2 and empty_placements == 1

                threats += 1 if threat_exists else 0
            
            return threats == 2

        # 3. Fork
        # Create a fork: two non-blocked lines for possible win
        for placement in range(1, 10):
            if self.board[placement] == DEFAULT:
                self.board[placement] = MY_TOKEN
                if _fork_exists(MY_TOKEN, placement):
                    return
                else:
                    self.board[placement] = DEFAULT

        # 4. Block opponent's fork
        for placement in range(1, 10):
            if self.board[placement] == DEFAULT:
                self.board[placement] = OPP_TOKEN
                if _fork_exists(OPP_TOKEN, placement):
                    self.board[placement] = MY_TOKEN
                    return
                else:
                    self.board[placement] = DEFAULT

        # 5. Play center
        if self.board[5] == DEFAULT:
            self.board[5] = MY_TOKEN
            return
        
        # 6. Play opposite corner
        if self.board[1] == DEFAULT and self.board[9] == OPP_TOKEN:
            self.board[1] = MY_TOKEN
            return
        elif self.board[3] == DEFAULT and self.board[7] == OPP_TOKEN:
            self.board[3] = MY_TOKEN
            return
        elif self.board[7] == DEFAULT and self.board[3] == OPP_TOKEN:
            self.board[7] = MY_TOKEN
            return
        elif self.board[9] == DEFAULT and self.board[1] == OPP_TOKEN:
            self.board[9] = MY_TOKEN
            return

        # 7. Play empty corner 
        empty_corners = [place for place in (1, 3, 7, 9) if self.board[place] == DEFAULT]
        if len(empty_corners) != 0:
            self.board[random.choice(empty_corners)] = MY_TOKEN
            return

        # 8. Play empty side
        empty_sides = [place for place in (2, 4, 6, 8) if self.board[place] == DEFAULT]
        if len(empty_sides) != 0:
            self.board[random.choice(empty_sides)] = MY_TOKEN

if __name__ == "__main__":
    while True:
        game = TicTacToe()
        # take turn 
        # make move
        # check win - break
        while not game.is_done():
            game.next_turn()

        print(game)

        print('\nWould you like to play another game? (y/n)')
        another_game = input().strip().lower()

        # ask if another game, if n - break
        while another_game not in ('y', 'n'):
            print('Please enter \'y\' or \'n\'.')
            print('Would you like to play another game? (y/n)')
            another_game = input().strip().lower()
        
        if another_game == 'n':
            break
