from typing import List

from data import DICTIONARY, LETTER_SCORES


def load_words() -> List[str]:
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, "r") as dictionary:
        data = [line.strip() for line in dictionary.readlines()]
        return data


def calc_word_value(word: str) -> int:
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES:
            score += LETTER_SCORES[letter.upper()]
    return score


def max_word_value(list_of_words: List[str] = load_words()) -> str:
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(list_of_words, key=lambda word: calc_word_value(word))


if __name__ == "__main__":
    list_of_words = load_words()
    word = list_of_words[42]

    print(f"The word '{word}' is worth {calc_word_value(word)} points.")
    print(
        f"The best word is '{max_word_value(list_of_words)}' with "
        f"{calc_word_value(max_word_value(list_of_words))} points."
    )
