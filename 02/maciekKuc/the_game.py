from data import DICTIONARY, LETTER_SCORES, POUCH
import random

#function for loading words
def draw():
    letters = []
    drawn = []
    i = 0
    while i < 7:
        n = random.randrange(0,len(POUCH))
        if n not in drawn:
            drawn.append(n)
            letters.append(POUCH[n])
            i = i + 1
    return letters

print(random.randrange(0,len(POUCH)))
print(draw())

def score_calc(word):
    score = 0
    for letter in word:
        score = score + LETTER_SCORES[letter.upper()]
    return score

def check_word():
    with open(DICTIONARY, 'r') as file:
        words = DICTIONARY.read().split('\n')
        score = [0,'']
        for word in words:
            actuall_score = 0
            for letter in word:
                for scores in scrabble_scores:
                    if letter.upper() in scores[1]:
                        actuall_score = actuall_score + scores[0]
            if actuall_score > score[0]:
                score = [actuall_score, word]
        print('The highest score is %s and its for %s' % (score[0], score[1]))
        return score

while True:
    score = 0
    actuall_draw = draw()
    user_choice = input('You have drawn this set of letters: %s Please type a word out of them.' % actuall_draw)
    if user_choice in DICTIONARY:
        score = score_calc(user_choice)
    else:
        print('Wrong choice.')
    next_step = input('Your score is: %s.(Press "q" for quit, any other button to continue)' % score)
    if next_step == 'q':
        break

print(score_calc('abba'))