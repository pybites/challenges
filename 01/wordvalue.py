from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as fp:
        words_list = fp.read().split('\n')
    return words_list[:-1]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    letters = LETTER_SCORES.keys()
    word_score = 0
    for x in range(len(word)):
        letter = word[x].upper()
        if letter in letters:
            letter_score = LETTER_SCORES[letter]
            word_score += letter_score
    return word_score


def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    score_keeper = dict()
    if word_list is None:
        word_list = load_words()
    for word in word_list:
        score = calc_word_value(word)
        score_keeper[word] = score
    max_scores = max(score_keeper.values())
    for key, value in score_keeper.items():
        if value == max_scores:
            return key

if __name__ == "__main__":
    pass
