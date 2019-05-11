from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    dictionary_file_obj = open(DICTIONARY,"r")
    dictionary_list = dictionary_file_obj.readlines()
    dictionary_list = [each_word[:-1] for each_word in dictionary_list]
    return dictionary_list

def calc_word_value(input_word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    input_word_value = 0
    for each_letter in input_word:
        try:
            input_word_value += LETTER_SCORES[each_letter.upper()]
        except Exception as e:
            print("Exception Obtained in word: " + "'" +  input_word  + "'" +" and exception is " + str(e))

    return input_word_value

def max_word_value(words_list = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_word = ""
    for each_word in words_list:
        curr_word_value = calc_word_value(each_word)
        if curr_word_value > max_value:
            max_value = curr_word_value
            max_word = each_word
    return max_word

if __name__ == "__main__":
    dictionary_list = load_words()
    max_word = max_word_value(('bob', 'julian', 'pybites', 'quit', 'barbeque'))
    print("Word with Maximum Value : " + max_word)

    