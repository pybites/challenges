from data import DICTIONARY, LETTER_SCORES


def load_words(dictionary_path=DICTIONARY):
    """Load dictionary into a list and return list"""
    with open(dictionary_path, 'r') as f:
        words = [word.strip() for word in f.readlines() if word.strip()]
    return words


def calc_word_value(word, letter_scores=LETTER_SCORES):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(letter_scores.get(letter.upper(), 0) for letter in word)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)


if __name__ == "__main__":
    best_word = max_word_value()
    score = calc_word_value(best_word)
    print(f"Best word is `{best_word}` with a score of {score}")
