
from data import DICTIONARY, LETTER_SCORES

def load_words():
    llist=[]
    fp=open('dictionary.txt','r')
    for i in fp.readlines():
        llist.append(i.strip())
    fp.close()    
    return llist
    

def calc_word_value(word):
    sum=0
    for j in word:
        sum=sum+(LETTER_SCORES.get(j.upper(),0))
    return sum
    
def max_word_value(l=load_words()):
    max=0
    a=""
    for i in l:
        num=calc_word_value(i)
        if max<num:
            max=num
            a=i
    return a

if __name__ == "__main__":
	pass

    
