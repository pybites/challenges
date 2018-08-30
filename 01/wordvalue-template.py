from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open('dictionary.txt', 'r') as dictionary:
        list_data = []
        data = dictionary.read()
        elsp = data.split()
        list_data.append(elsp)
    return list_data

def calc_word_value():
    temp = ['doss', 'dbos', 'current', 'mother', 'father']
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    for i in temp:
        join_word = ' '.join(i)
        join_word.split(' ')
        for k in join_word:

    return LETTER_SCORE
def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate

print(load_words())
print(calc_word_value())