from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    return [word.strip() for word in open(DICTIONARY)]


def calc_word_value(word_):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    clean_word = word_.replace('-', '') if '-' in word_ else word_

    return sum([LETTER_SCORES[char.upper()] for char in clean_word])


def max_word_value(word_list_=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    max_val = 0
    max_word = ''

    for word in word_list_:
        w_val = calc_word_value(word)
        if w_val > max_val:
            max_word = word
            max_val = w_val

    return max_word


if __name__ == "__main__":
    the_words = load_words()
    print(f'{the_words[9]}: score {calc_word_value(the_words[9])}')
    highscore = max_word_value(the_words)
    print(f'{highscore}: score {calc_word_value(highscore)}')
    print(max_word_value())
    print(max_word_value(['oggy', 'ikx']))
    # run unittests to validate
