from data import DICTIONARY, LETTER_SCORES

TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

def load_words():
    """Load dictionary into a list and return list"""
    L=[]
    f=open(DICTIONARY,"r")
    for word in f.readlines():
        L.append(word.strip())
    f.close()
    return L

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    letter_list = list(word.upper())
    for letters in letter_list:
    	word_value = word_value+LETTER_SCORES[letters]
    #print("word_value {} word {}".format(word_value,word))
    return word_value


def max_word_value(word_list=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_value=0
    D={}
    if word_list!=DICTIONARY:
        for i in range(len(word_list)):
    	    letter_list = list(word_list[i].upper())  
    	    for letters in letter_list:
    	        word_value = word_value + LETTER_SCORES[letters]
    	    D[word_list[i]] = word_value
        max_value=max(zip(D.values(),D.keys()))
    else:
  	fp=open(DICTIONARY, 'r')
    	for word in fp.readlines():
    	    word = word.strip()
    	    value = calc_word_value(word)
    	    D[word]=value
    	fp.close()
    	max_value=max(zip(D.values(),D.keys()))
    return max_value[1]

if __name__ == '__main__':
    word_value = calc_word_value('bob')
    max_value_word = max_word_value()
    max_word_value_1 = max_word_value(TEST_WORDS)
    print(word_value)
    print(max_value_word)
    print(max_word_value_1)
