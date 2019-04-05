import itertools
import os
import urllib.request
from collections import defaultdict, namedtuple, Counter
import random
import time

# Load necessary data
# Load dictionary if it does not exists
DICTIONARY = os.path.join('dictionary.txt')
if not os.path.isfile(DICTIONARY):
    urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

# scrabbles scores
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# Loading the letter pouch in here instead of data.py
Letter = namedtuple('Letter', 'name amount value')

distribution = [Letter(name='A', amount='9', value='1'), Letter(name='B', amount='2', value='3'), Letter(name='C', amount='2', value='3'), Letter(name='D', amount='4', value='2'), Letter(name='E', amount='12', value='1'), Letter(name='F', amount='2', value='4'), Letter(name='G', amount='3', value='2'), Letter(name='H', amount='2', value='4'), Letter(name='I', amount='9', value='1'), Letter(name='J', amount='1', value='8'), Letter(name='K', amount='1', value='5'), Letter(name='L', amount='4', value='1'), Letter(name='M', amount='2', value='3'), Letter(name='N', amount='6', value='1'), Letter(name='O', amount='8', value='1'), Letter(name='P', amount='2', value='3'), Letter(name='Q', amount='1', value='10'), Letter(name='R', amount='6', value='1'), Letter(name='S', amount='4', value='1'), Letter(name='T', amount='6', value='1'), Letter(name='U', amount='4', value='1'), Letter(name='V', amount='2', value='4'), Letter(name='W', amount='2', value='4'), Letter(name='X', amount='1', value='8'), Letter(name='Y', amount='2', value='4'), Letter(name='Z', amount='1', value='10')]

POUCH = list(''.join(
        list(letter.name * int(letter.amount) for letter in distribution)))

assert len(POUCH) == 98  # no wildcards in this simple game


def main():
    # Prints introduction
    print('=' * 20)
    print('Let us play scrabble game. You will draw 7 letters in a list of letters.')
    print('Check if you can get the best word, score will be based on [your score/best score]')
    print('=' * 20)
    print()

    # Draws 7 letters in the POUCH and apply lower method.
    print('Drawing Letters...')
    choice = input('Automatic draw? (Draw 7 letters automatically) (Y/N): ')
    if choice.lower() == 'y':
        time.sleep(1)
        letters = draw_letters()
    elif choice.lower() == 'n':
        letters = draw_samples(POUCH)
    else:
        raise TypeError
    letters_lower = [x.lower() for x in letters]
    print('Letters drawn: {}'.format(letters[:]))

    # Ask for user input for the word that can be created from the letters drawn
    guess, check = enter_word()
    while guess not in dictionary:
        print('== Enter another word as word is not in dictionary.')
        guess, check = enter_word()
    checking = check_letters(check, letters_lower)
    while not checking:
        print('== Enter Another Word, word has letters not in draw or exceed letter draw count.')
        guess, check = enter_word()
        checking = check_letters(check, letters_lower)
    guess_value = compute_word_value(guess.lower())

    print('You have entered {} (value: {})'.format(guess.upper(), guess_value))

    # Get best word possible from the drawn letters
    comp_word, comp_word_value = get_comp(letters)
    print('Optimal word possible: {} (value: {})'.format(comp_word.upper(), comp_word_value))

    # Calculates score based on word/best word
    print('You scored: {}'.format(round(guess_value/comp_word_value, 2)))


def draw_letters():
    """This draws letters from the POUCH"""
    letters = list(random.sample(POUCH, 7))
    return letters


def draw_samples(letter_bank=POUCH):
    """Check if we can use .pop() method to get samples one by one."""
    lst = []
    rem = 7
    while len(lst) != 7:
        cnt = input('Enter how many letters to draw: ')
        if len(lst) + int(cnt) > 7:
            print('you have drawn more than 7 letters, chose less')
            cnt = input('Enter how many letters to draw: ')
        for _ in range(int(cnt)):
            letter = letter_bank.pop(random.randint(0, len(letter_bank)-1))
            lst.append(letter)
        rem -= int(cnt)
        if rem > 0:
            print('You have drawn {} letter{}, {} left'.format(len(lst), 's' if len(lst) > 1 else '', (7-len(lst))))
            print('Current letters drawn: {}'.format(lst))
        else:
            print('You have drawn {} letters'.format(len(lst)))

    return lst


def enter_word():
    """User inputs a word and this function will return that word and the list in lower case"""
    guess = input('Form a valid word: ')
    return guess, list(guess.lower())


def check_letters(list1, list2):
    """Compares 2 lists, wherein list1 must contain all item in list 2, exact count"""
    c1, c2 = Counter(list1), Counter(list2)
    for k, n in c1.items():
        if n > c2[k]:
            return False
    return True


# Get Computer Score
def get_comp(letters):
    """Get best possible word from draw_letters()"""
    word = max_word_value(dictionary_words(letters))
    return word, compute_word_value(word)


# Supplement Functions
# Gets all possible combination in a list of letters
def get_all_possible_comb(draw):
    lst = []
    for i in range(1, len(draw)):
        lst += list(itertools.permutations(draw, r=i))
    return set([''.join(a).lower() for a in lst])


# Get the combinations present in the dictionary
def dictionary_words(draw):
    words = get_all_possible_comb(draw)
    return [x for x in words if x in dictionary]


# Gets word value based on scrabble letter scores
def compute_word_value(word):
    letters = list(word)
    upped = [x.upper() for x in letters]
    score = []
    for x in upped:
        try:
            score.append(LETTER_SCORES[x])
        except KeyError:
            continue
    return sum(score)


# Gets the word with the max word value
def max_word_value(words):
    """given a list of words return the word with the maximum word value"""
    word_bank = defaultdict(int)
    for word in words:
        word_bank[word] = compute_word_value(word)
    max_ = max(word_bank, key=word_bank.get)
    return max_


if __name__ == '__main__':
    main()


