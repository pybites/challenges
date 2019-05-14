#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def letters_picked_in_dict(letters_picked):
    letters_picked_dict = {}
    for letter in letters_picked:
        if letter in letters_picked_dict:
            letters_picked_dict[letter] = letters_picked_dict[letter] + 1
        else:
            letters_picked_dict[letter] = 1

    return letters_picked_dict


def draw_letters():
    return random.sample(POUCH, NUM_LETTERS)


def input_word(letters_picked_dict):
    user_word = raw_input("Enter a word that can be formed from the displayed letters and is meaningful : ")
    if len(user_word) == 0:
        return False

    print("User Entered Word is " + str(user_word))
    # Validate if User input word can be formed from the letters in Random Selected Letters
    letters_picked_dict_replica = letters_picked_dict.copy()
    for each_letter in user_word:
        if each_letter in letters_picked_dict_replica:
            letters_picked_dict_replica[each_letter] = letters_picked_dict_replica[each_letter] - 1
        else:
            print("[ERROR] : Your provided word cannot be formed from the selected Letters.")
            print("[ERROR] : Letter - " + str(each_letter) + "is not present in the list as many times as it is present in your input word")
            return user_word, False

    # Validate if the word is present in English Words Dictionary
    if user_word not in DICTIONARY:
        return user_word, False

    return user_word, True


def main():
    # Randomly pick Seven alphabets. They can be same. 
    letters_picked = draw_letters()
    print("Selected Letters : "  + str(letters_picked))

    # Store the picked letters in python Dictionary Form
    letters_picked_dict = letters_picked_in_dict(letters_picked)

    # Input from the user a word which can be formed from the selected letters and is present in dictionary and then validate whether it satisfies those conditions.
    user_word, validation_status = input_word(letters_picked_dict)
    if validation_status == False:
        print("Provided Word is InValid")
        return

    # # Calculate the value of user input word
    user_word_value = calc_word_value(user_word)
    print("Value of User Entered Word : " + str(user_word_value))

    # # Find all the possible words that can be formed from the selected letters and then among them find the one with highest value
    # max_word, max_value = max_word_possible(letters_picked)

    # # Calculate the score for User input Word
    # user_word_score = (user_word_value/max_value)*100
    # print(user_word_value)









if __name__ == "__main__":
    main()
