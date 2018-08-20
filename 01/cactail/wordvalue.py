from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    file_ = DICTIONARY
    with open(file_) as f:
        words = f.readlines()
        return [word.strip() for word in words]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word:
        if letter.isalpha():
            value += LETTER_SCORES[letter.capitalize()]
    return value


def max_word_value(list_of_words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_position = max([(pos, calc_word_value(word))
                         for pos, word
                         in enumerate(list_of_words)], key=lambda x: x[1])[0]
    return list_of_words[word_position]


if __name__ == "__main__":
    pass  # run unittests to validate
