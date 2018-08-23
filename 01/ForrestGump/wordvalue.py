from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as fd:
        data = map(str.strip, fd.readlines())
    
    return data


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(letter, 0) for letter in word.upper()])


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_score_word = ''
    max_score = 0
    for word in words:
        score = calc_word_value(word)
        if score > max_score:
            max_score_word, max_score = word, score
    
    return max_score_word


if __name__ == "__main__":
    pass
