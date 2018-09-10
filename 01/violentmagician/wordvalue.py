from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as datafile:
        data = datafile.read().splitlines() 
    data.sort()
    data = [ x.strip() for x in data ]
    return(data)

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return(sum([LETTER_SCORES[x] for x in list(word.upper())]))

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    values = [{'word':x,'value':calc_word_value(x)} for x in words]
    sorted_values = sorted(values,key= lambda k:k['value'], reverse=True)
    return sorted_values[0]['word']

if __name__ == "__main__":
    pass # run unittests to validate
