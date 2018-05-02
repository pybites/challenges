"""Calculate word values from dictionary."""

from data import DICTIONARY
from data import LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list."""
    with open(DICTIONARY) as g:
        words = g.read().split()
    return words


def calc_word_value(word):
    """Return scrabble word value.

    Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES.
    """
    score = 0
    word = word.upper()
    for c in word:
        if c not in LETTER_SCORES:
            continue
        else:
            c_score = int(LETTER_SCORES[c])
            score += c_score
    return score


def max_word_value(wordlist=load_words()):
    """Return the maximum word value from list.

    Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY
    """
    max_score = 0
    max_word = ""
    for word in wordlist:
        score = calc_word_value(word)
        if score <= max_score:
            continue
        else:
            max_score = score
            max_word = word
    return max_word

if __name__ == "__main__":
    words = load_words()
    print(words[len(words)-5:len(words)])
    print(LETTER_SCORES)
    print(calc_word_value('zyzzogeton'))
    print("The best scoring word is {} with a score of {}"
          .format(max_word_value(words),
                  calc_word_value(max_word_value(words))))
    print("The best scoring word is {} with a score of {}"
          .format(max_word_value(), calc_word_value(max_word_value())))
    words_two = ['Alpha', 'Beta', 'Gamma']
    print("The best scoring word is {} with a score of {}"
          .format(
              max_word_value(words_two),
              calc_word_value(max_word_value(words_two))
              ))
    # run unittests to validate
