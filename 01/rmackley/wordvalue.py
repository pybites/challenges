from data import DICTIONARY, LETTER_SCORES

def load_words(dict):
    """Load dictionary into a list and return list"""
    dict_list = []
    with open(dict) as f:
        for line in f:
            dict_list.append(line.rstrip())
    return (dict_list)

def calc_word_value(test_str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in test_str:
        if letter not in [".",",","-","_",":",";"]:
            score += LETTER_SCORES.get(letter.upper())
    return score

def max_word_value(words_list=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max = 0
    for item in load_words(words_list):
        val = calc_word_value(item)
        if val > max:
            max_str = item
            max = val
    return max_str

if __name__ == "__main__":
    pass # run unittests to validate
