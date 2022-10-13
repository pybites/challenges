from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as reader:
        return [line.strip() for line in reader.readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES[letter] for letter in word.upper())

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not word_list:
        words = load_words()
    else:
        words = word_list

    max_value = 0
    result = ''
    for word in words:
        word_value = calc_word_value(word)
        if word_value > max_value:
            max_value = word_value
            result = word
    return result

if __name__ == "__main__":
    words = load_words()
    print(max_word_value(words))
