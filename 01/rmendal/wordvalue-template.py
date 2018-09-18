from data import DICTIONARY, LETTER_SCORES
import re

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f: # open the file, read it, assign it to content
        content = f.read()

    """  list comporehension for words in content. If I return just this it would format like 
    '\n', 'U', 'N', 'E', 'X', 'E', 'C', 'R', 'A', 'T', 'E', 'D', '\n' also remove 2 hyphens in the list
    """
    content = [words.strip('-') for words in content]

    """ put the contents of content into an empty string. This will output all words with line breaks after each but
    still not in a python list.
    """
    content = ''.join(content)

    """ using regular expression library and the findall method looks for all words in the string and puts them in a 
    list which is exactly what we want here
    """
    words_list = re.findall(r'\w+', content)

    return words_list # returns the list


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    word = word.upper() # makes the word all upper case
    word = list(word) # breaks the word into a list so each char can be compared
    word_score = 0 # var for total score

    for k, v in LETTER_SCORES.items(): # for loop for each key and corresponding value in the dict
        for chars in word: # to iterate over each character in the given word
            if chars in k: # if the chars in word are in the dict keys
                word_score += v # add the corresponding dict value to word_score

    return word_score # return the final word_score


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    words = [x.upper() for x in list(words)]  # converts the tuple to a list and performs upper on it
    max_score = 0
    word_iter = 0
    best_word = ''

    while word_iter < len(words):
        word_score = 0
        word = words.pop()  # removes the last item in the list and assigns it to word as a string
        for k, v in LETTER_SCORES.items():  # for loop for each key and corresponding value in the dict
            for chars in word:  # to iterate over each character in the given word
                if chars in k:  # if the chars in word are in the dict keys
                    word_score += v  # add the corresponding dict value to word_score
                    if word_score > max_score: # this if holds onto the best word and score
                        max_score = word_score
                        best_word = word
        word_iter += 1
    return best_word.lower()  # returns the highest scoring word in lowwer case to appease the tests xP

if __name__ == "__main__":
    pass # run unittests to validate
