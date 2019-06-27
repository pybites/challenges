from data import DICTIONARY, LETTER_SCORES


def load_words():
    f = open(DICTIONARY, "r")
    word_list = [line.strip().upper() for line in f]
    f.close()
    return word_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter in LETTER_SCORES.keys():
            score += LETTER_SCORES[letter]
    return score

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words==None:
        words = load_words()
    
    maximum = ("None", 0)

    for word in words:
        score = calc_word_value(word)
        if score > maximum[1]:
            maximum = (word,score)
    return maximum[0]

if __name__ == "__main__":
    pass # run unittests to validate

print(max_word_value())