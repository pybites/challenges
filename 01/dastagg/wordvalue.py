from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        contents = file.read()
        words = contents.splitlines()
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    letter_to_score = [LETTER_SCORES[letter.upper()] for letter in list(word)
                                        if letter.upper() in LETTER_SCORES.keys()]
    return sum(letter_to_score)


def max_word_value(list_of_words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not list_of_words:
        list_of_words = load_words()

    word_to_score_list = [{'word': word, 'score': calc_word_value(word)}
                                                for word in list_of_words]

    sorted_words_to_score = sorted(word_to_score_list, key= lambda word_score: word_score['score'])

    return sorted_words_to_score[-1]['word']


if __name__ == "__main__":
    pass # run unittests to validate
