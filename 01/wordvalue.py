from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    return [word.strip() for word in open(DICTIONARY)]


def calc_word_value(word_):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum([LETTER_SCORES.get(char.upper(), 0) for char in word_])


def max_word_value(word_list_=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    return max(word_list_, key=calc_word_value)

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
