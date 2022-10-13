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

while True:
    score = 0
    best_score = 0
    best_pick = ''
    actuall_draw = draw()
    user_choice = input('You have drawn this set of letters: %s Please type a word out of them.' % actuall_draw)
    if user_choice in DICTIONARY:
        score = score_calc(user_choice)
    else:
        print('Wrong choice.')
    for word in DICTIONARY:
        working = [char.upper() for char in word]
        if all(item in actuall_draw for item in working):
            this_one = score_calc(word)
            if this_one > best_score:
                best_score = this_one
                best_pick = word
    print('Optimal score is %s and it,s for the word: %s' % (best_score, best_pick))
    next_step = input('Your score is: %s.(Press "q" for quit, any other button to continue)' % round(score / best_score * 100, 2))
    if next_step == 'q':
        break
