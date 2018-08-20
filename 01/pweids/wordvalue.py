from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    dictionary = []
    with open(DICTIONARY) as file:
        for word in file:
            dictionary.append(word.strip())
    return dictionary

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(letter.capitalize(),0) for letter in word) 

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    longest_word = ('', 0)
    for word in words:
        val = calc_word_value(word)
        if val > longest_word[1]:
            longest_word = (word, val)
    return (longest_word[0])

if __name__ == "__main__":
    pass # run unittests to validate
