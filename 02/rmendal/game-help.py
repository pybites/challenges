#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

'''Requirements / steps
Last time we provided unittests and a guiding template. We received feedback that this was a bit too stringent.
Therefore we provide two templates this time: game-help.py and game-nohelp.py

We load in the necessary data structures to focus on the game:

# Note that DICTIONARY is a set for O(1) lookups
from data import DICTIONARY, LETTER_VALUES, POUCH
Draw 7 random letters from POUCH.

As said POUCH is given and contains a distribution of Scrabble letters so that the player gets enough vowels
(equally drawing A-Z makes it extremely hard because you need more vowels to make words):

['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C',
'D', 'D', 'D', 'D', ...]
Ask the player to form a word with one or more of the 7 letters of the draw. Validate input for:

1) all letters of word are in draw;
2) word is in DICTIONARY.
Calculate the word value and show it to the player.

To focus on this challenge we re-use two methods from the previous challenge for this: calc_word_value and max_word_value.

Calculate the optimal word (= max word value) checking all permutations of the 7 letters of the draw, cross-checking
the DICTIONARY set for valid ones. This is a bit more advanced, but allows you to score the player (next).

Show the player what the optimal word and its value.

Give the player a score based on the previous steps, basically: player_score / optimal_score.

Bonus (not required)
The optimal solution calculation might be a bit difficult for some, that's why we stop here. But if you are feeling
creative you might consider expanding this game:

Keep scores in a shelve (file, db) and notify the player when a new record is reached.

Work with hints and bonuses: hints cost x points, give a bonus of y points, for example when a 7 letter word is created
(complete draw exhausted).

Make a simple web, mobile app or pygame.

'''

from itertools import permutations
import random
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    lett_draw = random.choices(POUCH, k=NUM_LETTERS)
    return (lett_draw)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    user_word = input('Enter a word with one or more of the 7 letters of the draw: ').upper()
    user_word = list(user_word)
    _validation(user_word, draw)
    return (user_word)


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    for letter in word:
        assert letter in draw

    temp_word = ''.join(word).lower()
    assert temp_word in DICTIONARY

    return(word)


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    #return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)
    #word = word.upper()  # makes the word all upper case if it's not already
    #word = list(word)  # breaks the word into a list so each char can be compared
    word_score = 0  # var for total score

    for k, v in LETTER_SCORES.items():  # for loop for each key and corresponding value in the dict
        for chars in word:  # to iterate over each character in the given word
            if chars in k:  # if the chars in word are in the dict keys
                word_score += v  # add the corresponding dict value to word_score

    return word_score  # return the final word_score

# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    n = len(draw)
    word_list = []

    while n > 0:
        perm = _get_permutations_draw(draw, n)
        for w in DICTIONARY:
            for x in perm:
                if x == w and word_list.count(x) == 0:
                    word_list.append(x)
        n -= 1
    return word_list


def _get_permutations_draw(draw, n):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    perms = [''.join(i).lower() for i in permutations(draw, n)]  # returns permutations of draw, make it lower because the DICTIONARY is.
    return perms

# From challenge 01:
def max_word_value(words):
    #calculate the highest scoring word of all possible words
    max_score = 0
    best_word = ''
    words_len = len(words)

    while words_len > 0: #loop iterates over length of list
        word_score = 0
        word = words.pop().upper() # removes the last item in the list and assigns it to word as a string, upper to match letter scores
        for k, v in LETTER_SCORES.items():  # for loop for each key and corresponding value in the dict
            for chars in word:  # to iterate over each character in the given word
                if chars in k:  # if the chars in word are in the dict keys
                    word_score += v  # add the corresponding dict value to word_score
                    if word_score > max_score:  # this if holds onto the best word and score
                        max_score = word_score
                        best_word = word
        words_len -= 1
    return best_word.lower()  # returns the highest scoring word in lower case



def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters() # Works
    print('Letters drawn: {}'.format(', '.join(draw))) # Works

    word = input_word(draw) #Works
    word_score = calc_word_value(word) #Works
    print('Word chosen: {} (value: {})'.format(word, word_score)) # Works

    possible_words = get_possible_dict_words(draw) # Works

    max_word = max_word_value(possible_words)

    max_word_score = calc_word_value(list(max_word.upper()))
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    print('Word Score is: ' + str(word_score))
    print('Max Word Score is: ' + str(max_word_score))
    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
