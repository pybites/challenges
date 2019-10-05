from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    totalwords = []
    with open('dictionary.txt') as fileobj:
        for data in fileobj:
            totalwords.append(data.strip())
    return totalwords


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    if "-" in word:
        word = word.replace("-", "")
    return sum([LETTER_SCORES[data.upper()] for data in word])


def max_word_value(args=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    def func(x): return max(x.values())
    if args:
        data = {data: calc_word_value(data) for data in args}
    else:
        total_words = load_words()
        data = {value: calc_word_value(value) for value in total_words}
    value = func(data)
    for key, val in data.items():
        if val == value:
            return key


if __name__ == "__main__":
    pass  # run unittests to validate
