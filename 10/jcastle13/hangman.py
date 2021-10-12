from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


def guessWord(guess):
    print("Check if", guess, "is the correct guess here")
    exit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    print("Welcome to the game of Hangman")
    #print("word:", word)

    # Debug - Figure out how to detect a char in the word
    tempChar = 'a'
    lowerWord = word.lower()
    # Store all the letters that each player has tried
    triedLettersPlayer01 = []
    triedLettersPlayer02 = []
    usedLetters = {}
    #foundLetters = [False] * len(word)
    foundLetters = [None] * len(word)
    foundLettersPlayer02 = [False] * len(word)

    counter = 0
    for symbol in word:
        if ' ' == symbol:
            foundLetters[counter] = ' '
        elif '-' == symbol:
            foundLetters[counter] = '-'
        else:
            foundLetters[counter] = PLACEHOLDER
        counter += 1

    print("Allowed guesses:", ALLOWED_GUESSES)
    print("The word:\n", ' '.join(foundLetters))

    # sample call to hang_graphics
    wrongGuesses = 0

    for i in range(ALLOWED_GUESSES):
        tempChar = input("Enter a letter: ")
        index = 0
        foundLetter = False
        if tempChar not in usedLetters.keys():
            usedLetters[tempChar] = False
            for letter in lowerWord:
                if tempChar == letter:
                    #print("The letter", tempChar, "is found at:", index)
                    foundLetters[index] = word[index]
                    foundLetter = True
                index += 1
        if foundLetter == False and usedLetters[tempChar] == False:
            print(HANG_GRAPHICS[wrongGuesses])
            wrongGuesses += 1
        usedLetters[tempChar] = True
        print(' '.join(foundLetters))
        print("Would you like to take a guess?")
        if input("> ") == 'yes':
            userGuess = input("Enter your guess: ")
            guessWord(userGuess)

    print("wrongGuesses:", wrongGuesses)
    if wrongGuesses != ALLOWED_GUESSES:
        print("The number of guesses have run out.\nWould you like to take a guess what the word is?")
        userGuess = input("> ")
        # Check if the guess is correct or not (TODO: Call a function here)
        guessWord(userGuess)
    else:
        print("Sorry but you did not win :(")
