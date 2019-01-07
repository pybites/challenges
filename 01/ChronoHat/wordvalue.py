from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    
    with open(DICTIONARY) as d:
        words = d.read().splitlines()

    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    'Initialize score, capitalize word'
    score = 0
    word = word.upper()
    
    'Add score per letter'
    for letter in word:
        if letter.isalpha():
            score += LETTER_SCORES[letter]

    return score

def max_word_value(word_list = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    'Initialize high score'
    max_score = 0

    'Calculate the score for each word'
    for word in word_list:
        score = calc_word_value(word)

        'Capture the largest word (so far) and its score'
        if score > max_score:
            max_score = score
            best_word = word

    return best_word

if __name__ == "__main__":
    import test_wordvalue as test
    test()

