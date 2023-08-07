from data import DICTIONARY, LETTER_SCORES

def load_words() -> list:
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as word_file:
        return [line.strip() for line in word_file.readlines()]

def calc_word_value(word: str) -> int:
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0

    try:
        for letter in word:
            score += LETTER_SCORES[letter.upper()]

        return score
    except:
        return 0

def max_word_value(words: list = None) -> str:
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()

    return max(words, key=calc_word_value)

if __name__ == "__main__":
    import unittest
    from test_wordvalue import TestWordValue

    unittest.main()