from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return f.read().strip().split('\n')

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0

    for letter in word:
        if letter.upper() in LETTER_SCORES.keys():
            score += LETTER_SCORES[letter.upper()]
        else:
            return 0
        
    return score

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    maxWord = ''
    maxValue = 0

    for word in words:
        value = calc_word_value(word)
        
        if value > maxValue:
            maxWord = word
            maxValue = value
        elif value == maxValue:
            maxWord += f', {word}'
        else:
            continue

    return maxWord

if __name__ == "__main__":
    pass # run unittests to validate
