import itertools
import random
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    return random.sample(POUCH, NUM_LETTERS)

def input_word(draw):
    word_choosen_by_player = input("Quel est votre proposition de mot ? ")
    while not (_validation(word_choosen_by_player, draw)):
        print("\n*******************\nMauvais choix de mot. \nUne des lettres du mot n'est pas dans votre tirage ou le mot que vous proposez n'existe pas !")
        word_choosen_by_player = input("Veuillez proposer un mot valide issu du dictionnaire francais avec les lettres de votre tirage... -> ")
    return word_choosen_by_player


def _validation(word, draw):
    #return (False not in [letter.upper() in draw for letter in word]) and (word in DICTIONARY)
    if (False not in [letter.upper() in draw for letter in word]) and (word in DICTIONARY):
        return True
    else:
        raise ValueError

# From challenge 01:
def calc_word_value(word):
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def get_possible_dict_words(draw):
    permutations = ["".join(word).lower() for word in _get_permutations_draw(draw)]
    return set(permutations) & set(DICTIONARY)


def _get_permutations_draw(draw):
    for i in range(1, NUM_LETTERS+1):
        yield from list(itertools.permutations(draw, i))

def max_word_value(words):
    return max(words, key=calc_word_value)


def main():
    print("Bienvenue dans mon jeu du Scrabble \n****************************\n")
    draw = draw_letters()
    print('Voici votre tirage (au hasard) : {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Vous proposez : {} (points: {})'.format(word, word_score))
    print("*****************************************")

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Le mieux que vous auriez pu proposer était : {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('Votre score : {:.1f}%'.format(game_score))


if __name__ == "__main__":
    main()

