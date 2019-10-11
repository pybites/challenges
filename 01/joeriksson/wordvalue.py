from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    return_list = []
    with open(DICTIONARY, "r") as file:
        for line in file:
            return_list.append(line.strip("\n"))

    return return_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    scores = 0
    for char in word:
        try:
            scores += LETTER_SCORES[char.upper()]
        except KeyError:
            continue

    return scores


def max_word_value(list_of_words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    value_dict = {}

    for word in list_of_words:
        value_dict[word] = calc_word_value(word)
    max_word = sorted(value_dict, key=value_dict.get, reverse=True)
    return "".join(max_word[:1])
