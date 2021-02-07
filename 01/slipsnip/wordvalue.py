import re
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dictionary:
        return dictionary.read().splitlines()

def calc_word_value(word: str) -> int:
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    # breakpoint()
    # remove trailing spaces and any non alphabetic char
    upper_word = word.upper().rstrip()
    upper_word = re.sub(r'[^a-zA-Z]', '', upper_word)
    """Loop through LETTER_SCORES filtering for (letter,score) pairs
        where letter is in word returning the coresponding score
        for each filtered score pair (letter,score)"""
    scores = [LETTER_SCORES.get(letter) for letter in upper_word]
    return sum(scores)

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return list(sorted(words, key=calc_word_value, reverse=True))[0]

if __name__ == "__main__":
    pass  # run unittests to validate
