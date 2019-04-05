import sys
from os import name, system
from string import ascii_lowercase
from typing import List, Set

from graphics import hang_graphics
from movies import get_movie as get_word  # keep interface generic

ASCII: List[str] = list(ascii_lowercase)
HANG_GRAPHICS: List[str] = list(hang_graphics())
ALLOWED_GUESSES: int = len(HANG_GRAPHICS)
PLACEHOLDER: str = "_"


class Hangman(object):
    def __init__(self, word: str) -> None:
        self.guessed: Set[str] = set()
        self.word: str = word
        self.tries: int = 1

    def __str__(self) -> str:
        return HANG_GRAPHICS[self.tries - 1] + "\n" + "".join(self.mask)

    def clear_screen(self) -> None:
        """Clears the screen"""
        _: int = system("cls" if name == "nt" else "clear")
        info: str = f"tries: {self.tries}/{ALLOWED_GUESSES}"
        print(f"{'Welcome to Hangman!':^50}")
        print()
        print(f"{info:>50}")
        print(f"guesses: {', '.join(self.guessed):<50}")
        print()

    def guess(self, letter: str) -> bool:
        if letter in self.guessed:
            raise ValueError(f"Already guess {letter} before!")

        matched: bool = False
        for l in word:
            if l.lower() == letter.lower():
                matched = True
            self.guessed.add(letter)

        return True if matched else False

    @property
    def mask(self) -> str:
        masked: List[str] = []
        for letter in self.word:
            if letter.lower() in self.guessed:
                masked.append(letter)
            elif letter == " ":
                masked.append(" ")
            else:
                masked.append(PLACEHOLDER)
        return " ".join(masked)

    def play(self) -> None:
        self.clear_screen()
        try:
            while self.tries < ALLOWED_GUESSES:
                print(self)
                player_guess: str = input("\nWhat is your guess? ").lower()
                if len(player_guess) > 1:
                    self.clear_screen()
                    print("Only one character at a time!")
                    continue
                elif not player_guess:
                    self.clear_screen()
                    print("You must enter at least one character!")
                    continue
                else:
                    try:
                        result: bool = self.guess(player_guess)
                        if self.status:
                            self.clear_screen()
                            print("You've won!")
                            print(self)
                            exit()
                        elif result:
                            self.clear_screen()
                            print("Correct!")
                        else:
                            self.tries += 1
                            self.clear_screen()
                            print("Sorry, try again!")
                    except ValueError as e:
                        self.clear_screen()
                        print(e)

            print(HANG_GRAPHICS[-1])
            print(f"The phrase/word was {word}")
            print("Better luck next time!")
        except KeyboardInterrupt:
            self.stop()

    def reset(self) -> None:
        self.word = get_word()
        self.guessed = set()
        self.tries = 1
        self.clear_screen()

    @property
    def status(self) -> bool:
        return True if PLACEHOLDER not in self.mask else False

    def stop(self) -> None:
        self.clear_screen()
        print("Goodbye!")
        exit()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        word: str = sys.argv[1]
    else:
        word = get_word()
    print(word)

    game = Hangman(word)
    game.play()
