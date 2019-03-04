from data import *

testWords = ['HELLO','ZEBRA','COFFEE','EMPLOYMENT','SCHOOL']

def calcWordValue(word):

    score = 0
    wordList = list(word)

    for countThree in range(len(wordList)):
        letterList = [x[1] for x in scrabble_scores]
        #print('HERE IS THE LETTER LIST IN THE LOOP: ' + str(letterList))
        for countFour in range(len(letterList)):
            string = letterList[countFour]
            for countFive in range(len(string)):
                if string[countFive] == wordList[countThree]:
                    #print("WE FOUND LETTER: " + string[countFive])
                    score += scrabble_scores[countFour][0]
                    #print('THIS LETTER HAS A SCORE OF: ' + str(scrabble_scores[countFour][0]))
    return score


for count in range(len(testWords)):
    print('--------')
    print('The score of word: ' + str(testWords[count]) + ' is: ' + str(calcWordValue(testWords[count])))
