from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


def guessWord(guess):
    answer = word.lower()
    guess = guess.lower()
    print("Check if", guess, "matches with", answer)
    if guess == answer:
        print("***************************")
        print("* You have won the game!! *")
        print("***************************")
    else:
        print("Sorry but you did not win :(")
        print("The answer was:", word)
    exit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    print("**********************************")
    print("* Welcome to the game of Hangman *")
    print("**********************************")

    usedLetters = {}
    foundLetters = [None] * len(word)

    counter = 0
    for symbol in word:
        if ' ' == symbol:
            foundLetters[counter] = ' '
        elif '-' == symbol:
            foundLetters[counter] = '-'
        elif ':' == symbol:
            foundLetters[counter] = ':'
        elif "'" == symbol:
            foundLetters[counter] = "'"
        elif '.' == symbol:
            foundLetters[counter] = '.'
        else:
            foundLetters[counter] = PLACEHOLDER
        counter += 1

    print("You have", ALLOWED_GUESSES, "allowed guesses.")
    print("The word:")
    print(' '.join(foundLetters), "\n")

    wrongGuesses = 0

    for i in range(ALLOWED_GUESSES):
        tempChar = input("Enter a letter: ")
        index = 0
        foundLetter = False
        if tempChar not in usedLetters.keys():
            usedLetters[tempChar] = False
            for letter in word.lower():
                if tempChar == letter:
                    foundLetters[index] = word[index]
                    foundLetter = True
                index += 1
        if foundLetter == False and usedLetters[tempChar] == False:
            print(HANG_GRAPHICS[wrongGuesses])
            wrongGuesses += 1
        usedLetters[tempChar] = True
        print(' '.join(foundLetters))

    if wrongGuesses != ALLOWED_GUESSES:
        print("The number of guesses have run out.\nWould you like to take a guess what the word is?")
        userGuess = input("> ")
        guessWord(userGuess)
    else:
        print("Sorry but you did not win :(")
        print("The answer was:", word)
