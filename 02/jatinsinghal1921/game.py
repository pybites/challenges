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
def max_word_value(words_list):
    """Calc the max value of a collection of words"""
    max_word = 0
    max_value = 0
    for each_word in words_list:
        each_word_value = calc_word_value(each_word)
        if each_word_value > max_value:
            max_value = each_word_value
            max_word = each_word

    return max_word, max_value


# Random Selection of Letters from the Pouch [List of repetitive Alphabets]
def draw_letters():
    return random.sample(POUCH, NUM_LETTERS)


# Storing the picked letters in dictionary format. 
def letters_picked_in_dict_form(letters_picked):
    letters_picked_dict = {}
    for letter in letters_picked:
        if letter in letters_picked_dict:
            letters_picked_dict[letter] = letters_picked_dict[letter] + 1
        else:
            letters_picked_dict[letter] = 1

    return letters_picked_dict


# Selecting the words in dictionary which can be formed from the picked letters
def possible_words_in_dictionary(letters_picked_dict):
    list_of_possible_words = []
    for each_word in DICTIONARY:
        '''storing the status of each word in a variable. If this variable is set to 0 while traversing each letter 
        of it, it implies that the word cannot be formed from the selected letters'''
        can_form = 1
        # Create a copy since dictionary are passed by refernce so working on passed argument will modify actual dictionary
        letters_picked_dict_replica = letters_picked_dict.copy()
        for each_letter in each_word:
            if each_letter.upper() in letters_picked_dict_replica:
                letters_picked_dict_replica[each_letter.upper()] = letters_picked_dict_replica[each_letter.upper()] - 1
                if letters_picked_dict_replica[each_letter.upper()] == 0:
                    del letters_picked_dict_replica[each_letter.upper()]
            else:
                can_form = 0
                break
        if can_form == 1:
            list_of_possible_words.append(each_word)

    return list_of_possible_words


# Asking user for input word and then validating whether it can be formed from the drawn letters and is also present in our Predefined Word Dictinary.
def input_word(letters_picked_dict):
    user_word = input("Enter a word that can be formed from the displayed letters and is meaningful : ")
    
    if len(user_word) == 0:
        print("[ERROR] : You haven't entered any word.")
        return user_word, False

    # Validate if User input word can be formed from the letters in Random Selected Letters
    letters_picked_dict_replica = letters_picked_dict.copy()
    for each_letter in user_word:
        if each_letter.upper() in letters_picked_dict_replica:
            letters_picked_dict_replica[each_letter.upper()] = letters_picked_dict_replica[each_letter.upper()] - 1
        else:
            print("[ERROR] : Your provided word cannot be formed from the selected Letters.")
            print("[ERROR] : Letter - " + str(each_letter) + " is not present in the list as many times as it is present in your input word")
            return user_word, False

    # Validate if the word is present in English Words Dictionary
    if user_word.lower() not in DICTIONARY:
        return user_word, False

    return user_word, True


def main():
    # Randomly pick Seven alphabets. They can be same. 
    letters_picked = draw_letters()
    print("Selected Letters : "  + str(letters_picked))

    # Store the picked letters in python Dictionary Form
    letters_picked_dict = letters_picked_in_dict_form(letters_picked)

    # Find all the possible words that can be formed from the selected letters and then among them find the one with highest value
    possible_dictionary_words = possible_words_in_dictionary(letters_picked_dict)
    max_word,max_value = max_word_value(possible_dictionary_words)

    # Input from the user a word which can be formed from the selected letters and is present in dictionary and then validate whether it satisfies those conditions.
    user_word, validation_status = input_word(letters_picked_dict)
    if validation_status == False:
        print("Provided Word is InValid")
        return

    # Calculate the value of user input word
    user_word_value = calc_word_value(user_word)

    # Print User Word,its value, Max Word and its value
    print("User entered word : " + user_word) 
    print("Value of User Entered Word : " + str(user_word_value) + "\n")
    print("Max Word : " + max_word)
    print("Max Word Value : " + str(max_value))

    # Calculate the score for User input Word
    user_word_score = (user_word_value/max_value)*100
    print("Score of User Word from list of possible words " + str(user_word_score))


if __name__ == "__main__":
    main()
