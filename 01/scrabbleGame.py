from data import *

testWords = []

def calcWordValue(word):

    score = 0
    wordList = list(word)

    for countThree in range(len(wordList)):
        letterList = [x[1] for x in scrabble_scores]
        for countFour in range(len(letterList)):
            stringList = letterList[countFour]
            for countFive in range(len(stringList)):
                if stringList[countFive] == wordList[countThree].upper():               # Quickly realised the system has to recognise upper and lower case.
                    score += scrabble_scores[countFour][0]

    return score

def dictTopWord(dict):

    scorelistCount = 0
    topThreeWordList = []
    topThreeScoreList = []

    scoreList = []                                                                      # Create empty scoreList to run concurrently with my dictionary list.
                                                                                        # Using this two dimensional array I can find the top score and print the relavent index.
    with open(dict,'r') as f:
        list = f.readlines()                                                            # The following creates a list by reading each line of my .txt file.
        list = [x.strip('\n') for x in list]                                            # This list comprehension is required to remove the '\r' from the list.

    for count in range(len(list)):                                                      # Now simply populate my scoreList with each corresponding word in the dictionary list.
        scoreList.append(calcWordValue(list[count]))

    for count in range(len(scoreList)):
        topThreeScoreList.append(scoreList[count])
        topThreeWordList.append(list[count])
        scorelistCount += 1
        if scorelistCount == 4:
            score1 = topThreeScoreList[0]
            score2 = topThreeScoreList[1]
            if score1 > score2:
                topThreeScoreList.pop(1)
                topThreeWordList.pop(1)
                scorelistCount = scorelistCount - 1
            else:
                topThreeScoreList.pop(0)
                topThreeWordList.pop(0)
                scorelistCount = scorelistCount -1

    print('=========================')
    print('')
    print('We have now iterated over the whole dictionary.')
    print('Here are your top scoring words.')
    print('')
    print('Top Words from given text file: ' + str(topThreeWordList))
    print('Corresponding word Scores: ' + str(topThreeScoreList))
    print('')
    print('==========================')


def main():

    print('Welcome to Frankies Scrabble Challenge Solution.')
    print('------------------------------------------------')
    print('')
    print('First of all lets give it a test, choose five words and find out what Scrabble scores they have.')
    word1 = input("What is your first word?")
    testWords.append(word1)
    word2 = input("What is your second word?")
    testWords.append(word2)
    word3 = input("What is your third word?")
    testWords.append(word3)
    word4 = input("What is your fourth word?")
    testWords.append(word4)
    word5 = input("What is your fifth word?")
    testWords.append(word5)

    print('')
    testInput = input('Great! Do you want to see your scores? y/n?')
    if testInput == 'y':
        for count in range(len(testWords)):
            print('--------')
            print('The score of word: ' + str(testWords[count]) + ' is: ' + str(calcWordValue(testWords[count])))
        print('')
        print('--------------------------')
        print('Ok, lets just move to the main event.')
    else:
        print('Ok, lets just move to the main event.')

    print('')
    print('GitHub Scrabble Challenge')
    print('=========================')
    print('')
    print('I was given a massive dictionary of words, and my task was to find the highest value words in the dictionary '
          'based on the given Scrabble scores.')

    dictInput = input('Do you want to see what the highest words were? y/n?')
    if dictInput == 'y':
        print('===================')
        print('')
        print('This will take a few minutes, bear with me, the list of words was massive!')
        print('')
        print('===================')
        dictTopWord(DICTIONARY)
    else:
        print('Well thanks for trying anyways. Bye!')

main()

