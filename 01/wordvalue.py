from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open('dictionary.txt', 'r') as dictionary:
        data = dictionary.read()
        elsp = data.split()
    return elsp

def calc_word_value(word):
    finish_count = 0
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    for k in list(word):
        count_word = LETTER_SCORES.get(str(k).upper())
        if count_word is not None:
            finish_count += count_word
    return finish_count

def max_word_value(my_dict=load_words()):
    max_count = 0
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    for i in my_dict:
        finish_count = calc_word_value(i)
        if max_count < finish_count:
            max_count = finish_count
    return max_count

if __name__ == "__main__":
    pass # run unittests to validate

print(load_words())
print(calc_word_value('Word'))
print(max_word_value(load_words()))