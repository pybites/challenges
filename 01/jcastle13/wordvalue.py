from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    #print("load_words method here")
    file = open("dictionary.txt", "r")
    temp_list = []
    for i in file:
        temp = str(i)
        temp_list.append(i.replace('\n',''))
    file.close()
    return(temp_list)
    pass

def calc_word_value(word=""):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    #print("calc_word_value method here")
    #print("word to calculate:", word)

    sum = 0
    for char in word:
        #print(char)
        if (char != "-"):
            sum = sum + LETTER_SCORES[str(char).upper()]

    #print("sum:",sum)
    return(sum)
    pass

def max_word_value(temp_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    #print("max_word_value method here")
    if (temp_list == None):
        #print("Entered the dictionary zone")
        list_dict = load_words()
        max_value = 0
        max_string = ""
        temp_value = 0
        for i in list_dict:
            #print(i)
            temp_value = calc_word_value(i)
            if (temp_value > max_value):
                max_value = temp_value
                max_string = i

        #print("max string is:", max_string)
        #print("value of string:", max_value)
        return(max_string)

    max_value = 0
    max_string = ""
    temp_value = 0
    for i in temp_list:
        #print(i)
        temp_value = calc_word_value(i)
        if (temp_value > max_value):
            max_value = temp_value
            max_string = i

    #print("max string is:", max_string)
    #print("value of string:", max_value)
    return(max_string)
    pass

if __name__ == "__main__":
    pass # run unittests to validate
