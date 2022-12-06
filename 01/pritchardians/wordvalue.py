from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as my_dict:
        return my_dict.read().splitlines()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    # print(f"word:{word}:")
    for letter in word:
        current_score = LETTER_SCORES.get(letter.upper())
        if current_score:
            score += current_score
    return score


def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = ""
    max_score = 0
    all_words = load_words()
    for word in all_words:
        score = calc_word_value(word)
        # print(f":{word}:{score}")
        if score > max_score:
            max_word = word
            max_score = score
    return max_word


if __name__ == "__main__":
    pass  # run unittests to validate

# Tests
# calc_word_value('abcde')
print(max_word_value())
