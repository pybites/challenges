from data import DICTIONARY, scrabble_scores

#function for loading words

def load_words():
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

load_words()