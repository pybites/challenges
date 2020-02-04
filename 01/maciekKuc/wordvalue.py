from data import DICTIONARY, LETTER_SCORES

#function for loading words

def load_words():
    with open(DICTIONARY, 'r') as file:
        words = file.read().split('\n')
        print(len(words))
        for line in file:
            print(line)

load_words()