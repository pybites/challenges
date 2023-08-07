from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = []
    # don't read the whole file into memory when you don't have too
    # files are iterable
    with open(DICTIONARY) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            words.append(line)
    return words

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = []
    for char in word:
        for val, lists in scrabble_scores:
            if char.lower() in lists.lower().split():
                value.append(val)

    return sum(value)

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    value_list = [calc_word_value(word) for word in words]
    return words[value_list.index(max(value_list))]

if __name__ == "__main__":
    pass # run unittests to validate
