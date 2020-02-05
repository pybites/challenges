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
        words = file.read().split('\n')
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

print(score_calc('abba'))