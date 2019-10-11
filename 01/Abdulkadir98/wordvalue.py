from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    file = open(DICTIONARY, "r")
    words = file.readlines()
    words = [word.rstrip() for word in words]
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word.upper().rstrip():
        score += LETTER_SCORES[letter]
    return score

def max_word_value(list = DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = ""
    max_value = 0
    for word in list:
        score = 0
        for letter in word.upper().rstrip():
            score += LETTER_SCORES[letter]
        if score > max_value:
            max_value = score
            max_word = word
    return max_word

if __name__ == "__main__":
     # run unittests to validate
     words = load_words()
     print(calc_word_value("benzalphenylhydrazone"))
     # print(max_word_value(words))
