from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY) as file:
        for word in file:
            words.append(word.rstrip('\n'))
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.isalpha():
            score += LETTER_SCORES[letter.upper()]
    return score

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_valued_word = ''
    max_score = 0
    for word in words:
        score = calc_word_value(word)
        if score > max_score:
            max_score = score
            max_valued_word = word
    return max_valued_word

if __name__ == "__main__":
    pass # run unittests to validate
