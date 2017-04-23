from string import ascii_lowercase, digits
import sys

from movies import get_movie as get_word  # keep interface generic
from jmtaysom_graphics import hang_graphics

ASCII = set(ascii_lowercase + digits)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, word):
        self.word = word
        self.word_set = set(letter.lower() for letter in self.word if letter.lower() in ASCII)
        self.guessed = set()
        self.graphics_gen = hang_graphics()
        self.graphics = next(self.graphics_gen)
        self.game_board = self.display_game_board()
        self.print_game_board()
        self.play_game()


    def play_game(self):
        """
        While the game is not over ask the user for a letter. Make sure it is
        a valid entry and hasnt already been guessed. If it is a bad guess then
        advance the gallows. Add the letter to the guessed letters, update the
        board, print the board and check for the end of the game.
        """
        while True:
            letter = input('Guess a letter: ').lower()
            if len(letter) > 1:
                print('Please only guess one letter at a time')
                continue
            elif letter in self.guessed:
                print('You have already guessed that letter')
                continue
            elif letter not in ASCII:
                print('please guess a letter')
                continue
            elif letter not in self.word_set:
                self.graphics = next(self.graphics_gen)
            self.guessed.add(letter)
            self.game_board = self.display_game_board()
            self.print_game_board()
            self.check_end_of_game()


    def check_end_of_game(self):
        """
        Check to see if the game is over.
        """
        if len(self.guessed - self.word_set) == 7:
            print('GAME OVER!')
            self.new_game()
        elif self.word_set.issubset(self.guessed):
            print('You Win!')
            self.new_game()

    def new_game(self):
        """
        Ask if the user wants to play a new game reinitialize the game
        or if not then quit the game.
        """
        response = input('Would you like to play a again? ')
        if response in {'Yes', 'yes', 'Y', 'y'}:
            self.__init__(get_word())
        elif response in {'No', 'no', 'N', 'n'}:
            sys.exit(1)
        else:
            self.new_game()

    def display_game_board(self):
        """
        For every letter in the word, check to see if it has been guessed.
        If so add it to the game board. Add all special characters to the
        board. For letters that haven't been guessed, display as an _
        :return:
        """
        display = ''
        for character in self.word:
            if character.lower() in self.guessed:
                display += character
            elif character.lower() not in ASCII:
                display += character
            else:
                display += '_'
        return display


    def print_game_board(self):
        """Print the gallows and the board"""
        print(self.graphics, '\n')
        print(self.game_board)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    #print(word)
    a = Hangman(word)

