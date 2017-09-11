#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
import itertools

NUM_LETTERS = 7


class UserBoard:
    letters = []

    def __init__(self):
        self.letters = random.sample(POUCH, NUM_LETTERS)

    def request_word(self):
        word = input('Form a valid word: ')
        if not self._word_from_letters(word):
            print('Please create a valid word from pouch letters.')
            word = self.request_word()
        elif not self._valid_word(word):
            print('Not a valid word.')
            word = self.request_word()
        return word

    def _word_from_letters(self, word):
        for letter in word:
            if letter.upper() not in self.letters:
                return False
        return True

    def print_letters(self):
        print('Letters drawm: {}'.format(', '.join(self.letters)))

    # cache DICTIONARY on initial read in data.py
    def _valid_word(self, word):
        return word.lower() in DICTIONARY

    def _get_possible_words(self):
        possible_words = []
        # possible to do w/o nested list?
        for x in range(1, len(self.letters) + 1):
            comb_lists = itertools.permutations(self.letters, x)
            for lis in comb_lists:
                if self._valid_word(''.join(lis)):
                    possible_words.append(''.join(lis))
        return possible_words


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters(amount):
    return random.sample(POUCH, NUM_LETTERS)

# comment out original module design - refactored to classes
# keeping original to test intricacies of module level vs class level
# def request_word(user_letters):
#     word = input('Form a valid word: ')
#     # refactor - class level variables in python to not pass user_letters??
#     if not _word_from_pouch(word, user_letters):
#         print('Please create a valid word from pouch letters.')
#         request_word(user_letters)
#     elif not _valid_word(word):
#         print('Not a valid word.')
#         request_word(user_letters)
#     else:
#         return word


# def _valid_word(word):
#     return word.lower() in DICTIONARY


# def _word_from_pouch(word, user_letters):
#     for letter in word:
#         if letter not in user_letters:
#             return False
#     return True


def main():
    # user_letters = draw_letters(NUM_LETTERS)
    # print('Letters drawn: {}'.format(', '.join(user_letters)))
    # user_word = request_word(user_letters)
    user_game = UserBoard()
    user_game.print_letters()
    user_word = user_game.request_word()
    word_value = calc_word_value(user_word)
    print('Your word, {}, is worth {} points!'.format(user_word, word_value))
    possible_words_list = user_game._get_possible_words()
    max_word = max_word_value(possible_words_list)
    max_word_points = calc_word_value(max_word)
    print('The optimal word, {}, is worth {} points!'
          .format(max_word, max_word_points))
    print('You scored {} points!'
          .format(((word_value / max_word_points) * 100)))


if __name__ == "__main__":
    main()
