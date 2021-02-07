from operator import itemgetter
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        result = [w.strip() for w in file.readlines()]
        return result


def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[c.upper()] for c in word if c.upper() in LETTER_SCORES])

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scores = [(word, calc_word_value(word)) for word in words]
    sorted_scores = sorted(scores, key=itemgetter(1), reverse=True)
    return sorted_scores[0][0]

if __name__ == "__main__":
    print(max_word_value())

