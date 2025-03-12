from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self, word: str) -> None:
        self.correct_word = word
        self.wrong_guesses = 0
        self.guesses = set()
    
    def __str__(self):
        return HANG_GRAPHICS[self.wrong_guesses] + f"\n{self.status}"
    
    @property
    def status(self):
        statusString = ""
        for c in self.correct_word:
            if c.lower() in self.guesses or c in [" ", "'", ".", ":"]:
                statusString += c
            else:
                statusString += PLACEHOLDER
        return statusString

    def guess(self):
        inputGuess = input("Guess any letter: ")
        if len(inputGuess) > 1:
            raise ValueError("Can't guess more than one letter")
        else:
            return inputGuess
        
    def play(self):
        while self.wrong_guesses < ALLOWED_GUESSES-1:
            print(str(self))
            if self.status == self.correct_word:
                break
            else:
                try:
                    charGuessed = self.guess()
                    if charGuessed not in self.guesses:
                        self.guesses.add(charGuessed)
                        if charGuessed not in self.correct_word.casefold():
                            self.wrong_guesses += 1
                    else:
                        print(f"Sorry. The letter '{charGuessed}' already taken. Try again.")
                except ValueError as e:
                    print(str(e))
        if self.wrong_guesses == ALLOWED_GUESSES-1:
            print(str(self) + f"\nToo bad. The word was {self.correct_word}.")
        else:
            print("Nice going. You guessed the correct word.")
        print("Thanks for playing.")    
# or use functions ...


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    #print(word)

    # init / call program
    game = Hangman(word)
    game.play()
