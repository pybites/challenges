from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    with open(f'../{DICTIONARY}', 'r') as dic:
        return [word.strip() for word in dic.readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum(
        [LETTER_SCORES[letter.upper()] for letter in word if letter.isalpha()]
    )

def max_word_value(words=[]):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    words = words if len(words) != 0 else load_words()

    top_score = 0
    best_word = ""
    for word in words:
        value = calc_word_value(word)
        if value > top_score:
            top_score = value
            best_word = word

    return best_word


if __name__ == "__main__":
    pass # run unittests to validate
