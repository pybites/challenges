import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    word_list = list()
    with open(DICTIONARY, 'r') as f:
    # with open('dictionary.txt', 'r') as f:
        for line in f:
            word_list.append(line.strip())
    return word_list


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    result = 0
    # LETTER_SCORES is a dict so loop over and get the dict value each time +=
    for letter in word:
        result += LETTER_SCORES.get(letter.upper(), 0)
        # print(result)
    return result


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    # use calc_word_value
    max_value = 0
    max_word = ""
    for w in words:
        word_value = calc_word_value(w)
        if word_value > max_value:
            max_value = word_value
            max_word = w
    return max_word


if __name__ == '__main__':
    words = load_words()
    max_word = max_word_value(words)
    print(calc_word_value('PyBites'))