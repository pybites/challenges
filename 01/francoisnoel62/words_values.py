DICTIONARY = 'dictionary.txt'

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                              for letter in letters.split()}

def load_words():
    with open(DICTIONARY) as f:
        return [word.replace('-', '') for word in f.read().split()]

def calc_word_value(word):
        return sum(LETTER_SCORES[letter.upper()] for letter in word)

def max_word_value(list=load_words()):
    max_value = 0
    word_with_max_value = ""
    for word in list:
        word_value = calc_word_value(word)
        if word_value > max_value:
            max_value = word_value
            word_with_max_value = word
    return word_with_max_value

