from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dict_file:
        dictionary = dict_file.read().splitlines()
    return dictionary

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for char in word.upper():
        if char.isalpha():
            score += LETTER_SCORES[char]
    return score 

def max_word_value(word_list=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_score = ('', 0)
    for word in word_list:
        score = calc_word_value(word)
        if score > max_score[1]:
            max_score = (word, score)
    return max_score[0]

if __name__ == "__main__":
    pass # run unittests to validate
