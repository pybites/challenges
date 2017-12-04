from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    words_list = []
    with open("dictionary.txt") as file:
        for word in file:
            words_list.append(word.replace("\n", ""))

    return words_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0

    if "-" in word:
        word = word.replace("-", "")

    for letter in word:
        word_value += LETTER_SCORES[letter.upper()]

    return word_value


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_scores = dict()
    world_values = []

    if words is None:
        words = load_words()

    for word in words:
        world_value = calc_word_value(word)
        word_scores[world_value] = word
        world_values.append(world_value)

    max_value = max(world_values)
    return word_scores[max_value]

if __name__ == "__main__":
    pass  # run unittests to validate
