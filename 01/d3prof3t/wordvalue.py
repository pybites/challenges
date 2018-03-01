from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as fp:
        return [line.strip() for line in fp.readlines()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    sum = 0
    for c in list(word):
        score = LETTER_SCORES.get(c.upper())
        if score:
            sum += score
    return sum


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        with open(DICTIONARY) as fp:
            words = [line.strip() for line in fp.readlines()]

    # iterate over the test_words and compare the
    # score of the words for each item
    score_word_map = {}
    for word in words:
        score = calc_word_value(word)
        score_word_map[score] = word
    lkp_keys = sorted(list(score_word_map.keys()))
    return score_word_map[lkp_keys.pop()]


if __name__ == '__main__':
    pass    # run the unit tests to validate
