from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open('dictionary.txt', 'r') as dictionary:
        data = dictionary.read()
        elsp = data.split()
    return elsp

def calc_word_value(word):
    finish_count = 0
    for k in list(word):
        count_word = LETTER_SCORES.get(k.upper(), 0)
        finish_count += count_word
    return finish_count

def max_word_value(my_dict=load_words()):
    max_count = 0
    for i in my_dict:
        finish_count = calc_word_value(i)
        if max_count < finish_count:
            max_count = finish_count
    return max_count

if __name__ == "__main__":
    words = load_words() # run unittests to validate
    print(max_word_value(words))

