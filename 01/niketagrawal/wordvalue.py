from data import DICTIONARY, LETTER_SCORES

def load_words():
    """
    Load words from the dictionary into a list and return the list

    Returns
    -------
    words: list
        list of words

    """
    with open(DICTIONARY) as d:
        word_list = []
        word_list = d.read().splitlines()
    return word_list


def calc_word_value(word: str):
    """
    Calculates the value of the word entered into function
    using imported constant mapping LETTER_SCORES

    Parameters
    ----------
    word : str
        A word from the dictionary

    Returns
    -------
    value: int
        The scrabble value for the word received as argument
    """
    value = 0
    word_upper = word.upper()
    for letter in word_upper:
        if ((ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122)):
            value += LETTER_SCORES[letter]
    return value

def max_word_value(*args):
    """
    Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY

    Returns
    -------
    max_value_word : str
        The word with the max value on Scrabble

    """
    value_list = []
    value_to_word = {}
    word_list = []
    if args:
        word_list = list(args[0])
    else:
        word_list = load_words() 
    for word in word_list:
        word_value = calc_word_value(word)
        value_list.append(word_value)
        value_to_word[word_value] = word
    value_list.sort()
    max_value = value_list[-1]
    max_value_word = value_to_word[max_value]
    return max_value_word

if __name__ == "__main__":
    max_value_word = max_word_value()
    print(max_value_word)
