#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
import re
from random import choice
from data import DICTIONARY, LETTER_SCORES, POUCH
from collections import defaultdict

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word: str) -> int:
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words: set) -> str:
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

# check if user input word can be made from the letters
def input_check(word: str, pouch: list) -> bool:
    matched = 0
    for letter in word:
        if letter.upper() in pouch:
            matched += 1
    return True if matched == len(word) else False

# check if it matches the dictionary
def dictionary_check(word: str, dictionary: set) -> None:
    print('\n+ User enterred a valid input. \n+ Checking score...')
    if re.search(word, ''.join(dictionary), re.IGNORECASE):
        score = calc_word_value(word)
        print('+ Word score is ', score)
        return score
    else:
        print('- Word is not found')
        return

# function to reduce and find the best word
def best_word(pouch: list, dictionary: set) -> int:
    print('+ Finding the best possible word...')

    # prepping
    spaced_dictionary = ' '.join(dictionary)
    pouch_letters = ''.join(pouch)
    condition_for_dictionary = re.compile('\s[%s]+\s' % pouch_letters, re.IGNORECASE )
    reduced_dictionary = condition_for_dictionary.findall(spaced_dictionary)
    found = []
    pouch_counter = defaultdict(int)

    for letter in pouch_letters:
        pouch_counter[letter.lower()] += 1

    for dictionary_word in reduced_dictionary:
        # to make sure we only use availible 7 chars
        dict_counter = defaultdict(int)
        passed = 0
        # this is recording the letters in dictionary word that has been reduced
        for record_letter in dictionary_word.strip():
            dict_counter[record_letter] += 1
        for record_letter in dict_counter:
            if dict_counter[record_letter] <= pouch_counter[record_letter]:
                passed += 1
        if passed == len(dict_counter):
            score = calc_word_value(dictionary_word)
            found.append((dictionary_word, score))
    if len(found) > 0:
        score = max(found, key=lambda x: x[1])
        print('\nThe best word is ', score)
        return score[1]
    else:
        print('Found nothing') #almost never runs
        raise ValueError('Something is clearly wrong...')

# main program
def main():
    """Intergrate functions into one main program """
    random_letters = [choice(POUCH) for i in range(NUM_LETTERS)]
    print(random_letters)
    given_word = input('\nForm a word from the above: ')

    # First, check from user
    if input_check(given_word, random_letters):
        player_score = dictionary_check(given_word, DICTIONARY)
    else:
        print('\n- Invalid input. Abort.')
        raise ValueError('This might be due to the player.')
    # Provide feed back
    best_score = best_word(random_letters, DICTIONARY)
    print('{:.2f}%'.format(player_score * 100/best_score), 'this is your score.')


if __name__ == "__main__":
    main()
