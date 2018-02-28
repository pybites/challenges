from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    word_list = list()
    with open(DICTIONARY, 'r') as fp:
        for line in fp.readlines():
            word_list.append(line.strip('\n'))
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter != '-':
            score = score + LETTER_SCORES[letter.upper()]
    return score


def max_word_value(dico=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scores = dict()
    word_list = dico or load_words()

    for word in word_list:
        word_score = calc_word_value(word)
        scores[word] = word_score

    maximum = max(scores, key=scores.get)
    return maximum


if __name__ == "__main__":
    pass
