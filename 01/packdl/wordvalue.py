from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        data = file.read()
        return data.splitlines()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(let.upper(),0) for let in word)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words == None:
        words = load_words()

    maxvalue = 0
    word = None

    for item in words:
        result = calc_word_value(item)
        if result > maxvalue:
            maxvalue = result
            word = item
    return word

if __name__ == "__main__":
    pass # run unittests to validate
