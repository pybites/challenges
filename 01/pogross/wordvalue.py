from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dictionary:
        list_of_words = [word[:-1] for word in dictionary]
        return list_of_words


def calc_word_value(word: str) -> int:
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES:
            score += LETTER_SCORES[letter.upper()]
    return score


def max_word_value(list_of_words: list=None) -> str:
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    best_word, best_score = "", 0
    for word in list_of_words or load_words():
        if calc_word_value(word) > best_score:
            best_word = word
            best_score = calc_word_value(word)
    return best_word


if __name__ == "__main__":
    list_of_words = load_words()
    word = list_of_words[5]

    print(f"The word \"{word}\" is worth {calc_word_value(word)} points.")
    print(f"The best word is \"{max_word_value(list_of_words)}\" with {calc_word_value(max_word_value(list_of_words))} points.")

    pass  # run unittests to validate
