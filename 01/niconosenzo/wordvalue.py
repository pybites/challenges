import operator
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    lista = []
    #return a list of words withoug newline character
    with open(DICTIONARY) as f:
        for line in f:
            lista.append(line)
    return [line.rstrip('\n') for line in lista]

def calc_word_value(word=""):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word:
        if isinstance(LETTER_SCORES.get(letter.upper()), int):
            value += LETTER_SCORES.get(letter.upper())
    return value


def max_word_value(lista=[]):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if  len(lista)== 0:
        lista = load_words()

    if len(lista) == 1:
        return lista[0]

    # Create a dictionary with all the words and their values:
    lista_values = {y: calc_word_value(y) for y in lista}
    # Use the operator library to sort the dict based on the values, it will return a list of tuples
    sorted_list = sorted(lista_values.items(), key=operator.itemgetter(1))

    return sorted_list[-1][0]

if __name__ == "__main__":
    pass # run unittests to validate
