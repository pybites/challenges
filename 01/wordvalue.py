from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    result = list()
    with open(DICTIONARY,mode='r') as f:
        for line in f:
            result.append(line.strip('\n'))
    return result

def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES
    ex: 
    word = dad >> value = 5 {'D': 2, 'A': 1}
    """
    return sum ([LETTER_SCORES[letter.upper()] for letter in list(word)])

def max_word_value(word_list=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    #words_val = [(word,calc_word_value(word)) for word in word_list]
    #sorted_list = sorted(words_val,key=lambda x: x[1],reverse = True)
    #return sorted_list[0][0]
    return max(word_list,key=calc_word_value)


if __name__ == "__main__":
    words = load_words()

    #pass # run unittests to validate
