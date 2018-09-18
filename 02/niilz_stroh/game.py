#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random as rd

print(rd.randint(0, 10))

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def get_7_chars():
    return [POUCH[rd.randint(0, len(POUCH))].lower() for _ in range(7)]

def possible_words(letters):
    words = []
    for word in DICTIONARY:
        if not all([letter in letters for letter in word]): continue
        else: words.append(word)
    words = [word for word in words if all([word.count(char) <= letters.count(char) for char in word])]
    return words


def main():
    letters = get_7_chars()
    possible_w = possible_words(letters)
    user_word = input(f"form a word from the letters '{letters}'")
    if not all([user_word.count(char) <= letters.count(char) for char in user_word]):
        print("sorry but have used some chars more often than they were given")
    else:
        print(f"your word scored {calc_word_value(user_word)} points.\n\
        The word with the highes score would have been '{max_word_value(possible_w)}'\n\
        with a score of {calc_word_value(max_word_value(possible_w))}")


if __name__ == "__main__":
    main()
