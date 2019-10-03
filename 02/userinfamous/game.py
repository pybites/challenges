#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
import re
from random import choice
from data import DICTIONARY, LETTER_SCORES, POUCH

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
    spaced = ' '.join(dictionary)
    letters = ''.join(pouch)
    words = re.compile('\s[%s]+\s' % letters, re.IGNORECASE )
    reduced = words.findall(spaced)
    results = []
    for word in reduced:
        score = calc_word_value(word)
        results.append((word, score))
    if len(results) > 0:
        score = max(results, key=lambda x: x[1])
        print('\nThe best word is ', score)
        return score
    else:
        print('Found nothing') #almost never runs
        return

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
        return
    
    # Provide feed back
    best_score = best_word(random_letters, DICTIONARY)
    print('{:.2f}%'.format(player_score * 100/best_score[1]), 'this is your score.')


if __name__ == "__main__":
    main()
