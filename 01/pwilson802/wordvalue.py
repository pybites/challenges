from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    res = []
    with open(DICTIONARY) as file:
        for line in file:
            res.append(line.strip())
    return res

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES:
            score += LETTER_SCORES[letter.upper()]
    return score

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_scores = {}
    for word in words:
        word_score = calc_word_value(word)
        word_scores[word] = word_score
    return max(word_scores, key=word_scores.get)

if __name__ == "__main__":
    from test_wordvalue import TestWordValue
