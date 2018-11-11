from data import DICTIONARY, LETTER_SCORES


with open(DICTIONARY) as fin:
    x = fin.read().splitlines()
    print(len(x))
    print(x[0])
    print(x[-1])