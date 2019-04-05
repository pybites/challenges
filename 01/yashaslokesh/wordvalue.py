from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(f'../{DICTIONARY}') as d:
        return [word.strip() for word in d.readlines()]

def calc_word_value(word):
    # Have to use letter.isalpha() because dashes exist in the dictionary words
    return sum([LETTER_SCORES[letter.upper()] for letter in word if letter.isalpha()])

def max_word_value(words=[]):

    words = words if len(words) != 0 else load_words()

    max_value = 0
    max_word = ""
    for word in words:
        word_value = calc_word_value(word)
        if word_value > max_value:
            max_word = word
            max_value = word_value
    return max_word
    
if __name__ == "__main__":
    pass # run unittests to validate