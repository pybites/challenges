#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
import itertools

NUM_LETTERS = 7

def draw_letter():
    """ Draw random letters from POUCH"""
    draw=random.sample(POUCH,NUM_LETTERS)
    return draw

def input_word(draw):
    print("Available letters")
    letters = ','.join(draw)
    print(letters)
    word = str(input("Enter a word"))
    return word

def _validate_input(word,draw):
    """ validate word against the letters drawn.
        Conditions to check.
        1) Only use letters of draw.
        2) Valid dictionary word."""
    word=word.strip('"')
    for char in word.upper():
        if char in draw:
            flag=True
        else:
            flag=False
            raise ValueError("entered character {} not in the list of drawn letters.".format(char))
    if word.lower() in DICTIONARY:
        flag=True
    else:
        flag=False
    return flag
   
def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    word=word.strip('"')
    letter_list = list(word.upper())
    for letters in letter_list:
        word_value = word_value+LETTER_SCORES[letters]
    return word_value


def max_word_value(word_list=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    word_value=0
    D={}
    if word_list!=DICTIONARY:
        for i in range(len(word_list)):
            word_value=0
            letter_list = list(word_list[i].upper())  
            for letters in letter_list:
                word_value = word_value + LETTER_SCORES[letters]
            D[word_list[i]] = word_value
        max_value=max(zip(D.values(),D.keys()))
    else:
        if word in DICTIONARY:
            word = word.strip()
            value = calc_word_value(word)
            D[word]=value
            max_value=max(zip(D.values(),D.keys()))
    return max_value[1], max_value[0]

def _letter_permutations(draw):
    D=dict()
    valid_words=[]
    for i in range(2,len(draw)+1):
        for item in itertools.permutations(draw,i):
            item=''.join(item)
            if item.lower() in DICTIONARY:
                valid_words.append(item)
    return valid_words



def main():
    draw=draw_letter()
    word = input_word(draw)
    print("validate the word being input")
    flag=_validate_input(word,draw)
    if flag:
        value_of_entered_word=calc_word_value(word)
        word=word.strip('"')
        print(word.upper(), value_of_entered_word)
        valid_words = _letter_permutations(draw)
        word, max_value=max_word_value(valid_words)
        print(word, max_value)
        if value_of_entered_word == max_value:
            print("Congratulations! You Win! :)")
        else:
            print("You Loose! Try Again")
        print("Your Score is {}/{}".format(value_of_entered_word, max_value))
    else:
        print("Word formed {} is not a valid word present in dictionary!".format(word))
    
if __name__ == "__main__":
    main()
