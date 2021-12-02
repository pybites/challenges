from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY) as dictionary:
        words = [word.strip("\n") for word in dictionary]
    return words

def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total_sum = 0
    for char in word:
        if char.upper() in LETTER_SCORES:
            total_sum += LETTER_SCORES[char.upper()]
    return total_sum
        

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_score = -1
    word_max = ""
    for word in words:
        score = calc_word_value(word)
        if score > word_score:
            word_score = score
            word_max = word
    return word_max

if __name__ == "__main__":
    pass # run unittests to validate
