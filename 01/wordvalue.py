from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    content = []
    with open(DICTIONARY) as dict:
        content = dict.read().splitlines()
        #can also iterate through the read w/ below code
        #for line in dict:
        #    content.append(line)
    return content


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word.upper():
        if type(LETTER_SCORES.get(letter)) is int:
            score = score + LETTER_SCORES.get(letter)
    return score


def max_word_value(input_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if input_list:
        return process_list(input_list)
    else:
        return process_list(load_words())


def process_list(list):
    max_value = 0
    for word in list:
        # this is to handle a list of similar valued words
        value = calc_word_value(word)
        # if value > max_value:
        #     largest_word_list = []
        #     largest_word_list.append(word)
        #     max_value = value
        # elif value == max_value:
        #     largest_word_list.append(word)
        if value > max_value:
            max_value = value
            largest_word = word
    return largest_word


if __name__ == "__main__":
    pass # run unittests to validate
